# Design a Transactional Key-Value Store

Design an in-memory key-value store that supports **nested transactions**.

The store should allow values to be written, deleted, committed, and rolled back. A transaction groups a set of changes so they can be applied atomically or discarded. Transactions may be nested, and each nested transaction should behave like a savepoint.

## Implement the `TransactionalKVStore` class

```python
class TransactionalKVStore:
    def get(self, key: str) -> int | None:
        pass

    def set(self, key: str, value: int) -> None:
        pass

    def delete(self, key: str) -> None:
        pass

    def begin(self) -> None:
        pass

    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass
```

## Operations

### `get(key)`
Return the current value associated with `key`. If the key does not exist, return `None`.

### `set(key, value)`
Set `key` to `value`.

### `delete(key)`
Remove `key` from the store if it exists.

### `begin()`
Start a new transaction. Transactions may be nested.

### `commit()`
Permanently apply all changes made in the current transaction.

- If the current transaction is nested, its changes should be merged into its parent transaction.
- If it is the outermost transaction, its changes should be applied to the main store.

### `rollback()`
Discard all changes made in the current transaction.

- If the current transaction is nested, only that transaction should be undone.
- Parent transactions should remain unchanged.

## Example

```python
db = TransactionalKVStore()

db.set("a", 1)
assert db.get("a") == 1

db.begin()
db.set("a", 2)
assert db.get("a") == 2
db.rollback()
assert db.get("a") == 1

db.begin()
db.set("a", 3)
db.commit()
assert db.get("a") == 3
```

Nested transactions:

```python
db.begin()      # Level 1
db.set("b", 10)
db.begin()      # Level 2
db.set("b", 20)
assert db.get("b") == 20
db.rollback()
assert db.get("b") == 10
db.commit()
assert db.get("b") == 10
```

## Constraints

- Up to `10^5` total operations
- Keys are non-empty strings
- Values are integers
- `commit()` and `rollback()` are only called when there is at least one active transaction
