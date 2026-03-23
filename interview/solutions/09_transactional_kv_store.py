from __future__ import annotations


_DELETED = object()


class TransactionalKVStore:
    """
    In-memory transactional key-value store with nested transactions.

    Design:
    - self._base: committed store
    - self._tx_stack: list[dict[str, object]]
      each dict stores only writes/deletes for that transaction level
    """

    def __init__(self) -> None:
        self._base: dict[str, int] = {}
        self._tx_stack: list[dict[str, object]] = []

    def get(self, key: str) -> int | None:
        for tx in reversed(self._tx_stack):
            if key in tx:
                value = tx[key]
                return None if value is _DELETED else value  # type: ignore[return-value]
        return self._base.get(key)

    def set(self, key: str, value: int) -> None:
        if self._tx_stack:
            self._tx_stack[-1][key] = value
        else:
            self._base[key] = value

    def delete(self, key: str) -> None:
        if self._tx_stack:
            self._tx_stack[-1][key] = _DELETED
        else:
            self._base.pop(key, None)

    def begin(self) -> None:
        self._tx_stack.append({})

    def commit(self) -> None:
        if not self._tx_stack:
            raise RuntimeError("No active transaction to commit")

        current = self._tx_stack.pop()

        if self._tx_stack:
            parent = self._tx_stack[-1]
            parent.update(current)
        else:
            for key, value in current.items():
                if value is _DELETED:
                    self._base.pop(key, None)
                else:
                    self._base[key] = value  # type: ignore[assignment]

    def rollback(self) -> None:
        if not self._tx_stack:
            raise RuntimeError("No active transaction to rollback")
        self._tx_stack.pop()


if __name__ == "__main__":
    db = TransactionalKVStore()
    db.set("a", 1)
    db.begin()
    db.set("a", 2)
    print(db.get("a"))  # 2
    db.rollback()
    print(db.get("a"))  # 1
