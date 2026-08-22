def remove_expired_items(items, today):
    """Remove expired items from a list of (name, expiry_date) tuples.

    Args:
        items: List of (name, expiry_date) tuples.
        today: The current date for comparison.

    Returns:
        List of (name, expiry_date) tuples where expiry_date > today
        (i.e., non-expired items).
    """
    result = []
    for i in range(len(items)):
        name, expiry_date = items[i]
        if expiry_date > today:
            result.append((name, expiry_date))
    return result