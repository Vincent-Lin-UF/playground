# Design a Dynamic Batch Inference Engine

You are given a simulated language model and must design a batch inference engine that serves multiple text generation requests efficiently.

The engine should process requests in batches, dynamically refill empty batch slots as requests finish, and stop each request when either:

- it has generated `max_tokens` new tokens, or
- the generated token equals `stop_token`

This problem models a simplified version of continuous batching used in LLM serving systems.

## Provided Class

```python
from typing import List

class SimulatedLLM:
    def generate_next_tokens(self, batch_prefixes: List[List[int]]) -> List[int]:
        pass
```

## Implement `BatchInferenceEngine`

```python
from typing import List, Callable

class BatchInferenceEngine:
    def __init__(self, model: SimulatedLLM, batch_size: int, stop_token: int):
        pass

    def submit_request(
        self,
        prompt_tokens: List[int],
        max_tokens: int,
        callback: Callable[[List[int]], None],
    ) -> None:
        pass

    def run(self) -> None:
        pass
```

## Requirements

- Fill available batch slots with waiting requests, up to `batch_size`
- Call `model.generate_next_tokens(...)` on the active batch
- Append one generated token to each active sequence
- Mark a request as complete if:
  - it has generated `max_tokens` new tokens, or
  - the generated token equals `stop_token`
- Invoke the callback immediately when a request completes
- Continue by filling newly available slots with waiting requests

## Example

```python
results = []
engine = BatchInferenceEngine(MockModel(always_return=5), batch_size=2, stop_token=0)
engine.submit_request([1, 2], max_tokens=3, callback=lambda s: results.append(s))
engine.run()

# results == [[1, 2, 5, 5, 5]]
```

## Constraints

- `1 <= batch_size <= 10^3`
- `1 <= max_tokens <= 10^4`
- `0 <= token <= 10^9`
- `0 <= stop_token <= 10^9`
- At most `10^5` requests may be submitted
- The sum of all generated tokens does not exceed `10^6`
