from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, List


class SimulatedLLM:
    def generate_next_tokens(self, batch_prefixes: List[List[int]]) -> List[int]:
        raise NotImplementedError


class MockModel(SimulatedLLM):
    """
    Helper model for local testing.

    If always_return is set, every request gets that same next token.
    Otherwise, tokens are taken from `sequence` in order for each batch step.
    """

    def __init__(self, always_return: int | None = None, sequence: list[int] | None = None) -> None:
        self.always_return = always_return
        self.sequence = sequence or []
        self.ptr = 0

    def generate_next_tokens(self, batch_prefixes: List[List[int]]) -> List[int]:
        if self.always_return is not None:
            return [self.always_return] * len(batch_prefixes)

        if self.ptr >= len(self.sequence):
            raise RuntimeError("MockModel sequence exhausted")

        token = self.sequence[self.ptr]
        self.ptr += 1
        return [token] * len(batch_prefixes)


@dataclass
class _Request:
    seq: list[int]
    max_tokens: int
    callback: Callable[[List[int]], None]
    generated: int = 0


class BatchInferenceEngine:
    def __init__(self, model: SimulatedLLM, batch_size: int, stop_token: int):
        self.model = model
        self.batch_size = batch_size
        self.stop_token = stop_token
        self._pending: deque[_Request] = deque()
        self._active: list[_Request] = []

    def submit_request(
        self,
        prompt_tokens: List[int],
        max_tokens: int,
        callback: Callable[[List[int]], None],
    ) -> None:
        self._pending.append(_Request(list(prompt_tokens), max_tokens, callback))

    def _fill_slots(self) -> None:
        while self._pending and len(self._active) < self.batch_size:
            self._active.append(self._pending.popleft())

    def run(self) -> None:
        while self._pending or self._active:
            self._fill_slots()
            if not self._active:
                break

            batch = [req.seq for req in self._active]
            next_tokens = self.model.generate_next_tokens(batch)

            still_active: list[_Request] = []

            for req, token in zip(self._active, next_tokens):
                req.seq.append(token)
                req.generated += 1

                done = token == self.stop_token or req.generated >= req.max_tokens
                if done:
                    req.callback(req.seq)
                else:
                    still_active.append(req)

            self._active = still_active


if __name__ == "__main__":
    results = []
    engine = BatchInferenceEngine(MockModel(always_return=5), batch_size=2, stop_token=0)
    engine.submit_request([1, 2], max_tokens=3, callback=lambda s: results.append(s))
    engine.run()
    print(results)  # [[1, 2, 5, 5, 5]]
