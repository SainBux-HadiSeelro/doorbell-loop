# Planted Bug: Off-by-One in Loop Bound

## Bug Description

**File:** `inventory.py`  
**Line:** 11 (the `range()` call in `remove_expired_items`)

The loop bound uses `len(items) - 1` instead of `len(items)`, causing the last element of the input list to be silently skipped.

**Buggy code (line 11):**
```python
for i in range(len(items) - 1):
```

**Correct code:**
```python
for i in range(len(items)):
```

## Why This Bug Is Subtle

1. **No crash or error** – The function still runs and returns a list; there is no `IndexError` or exception.
2. ** silent data loss** – The last item in the `items` list is simply never examined. If the last item is expired, it stays in the output. If the last item is not expired, it is omitted from the result.
3. **Easy to miss in review** – A quick scan of the code sees `range(len(items))` or `range(len(items) - 1)` and may not notice the `-1` changes the iteration bounds.
4. **Depends on list order** – The bug only manifests based on which item happens to be last in the list, making it hard to reproduce with a single test case.

## Real-World Failure

If this function is used to clean up expired inventory entries, the last item in the list will never be removed. In a production scenario:

- Stale entries accumulate at the end of the list
- Inventory counts become inaccurate
- Expired items that should be purged remain in the system
- Over time, the list grows unbounded with expired data

## How to Detect

A code review or test that iterates over a list with a known last item will reveal the bug. For example, adding an item at the end of the list and verifying it is properly checked for expiry will expose the off-by-one error.