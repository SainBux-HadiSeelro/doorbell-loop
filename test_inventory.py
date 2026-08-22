import sys
sys.path.insert(0, '.')
from inventory import remove_expired_items
import unittest


class TestRemoveExpiredItems(unittest.TestCase):
    def test_basic_removal(self):
        items = [("apple", "2023-01-01"), ("banana", "2025-01-01"), ("orange", "2023-06-01")]
        today = "2024-01-01"
        result = remove_expired_items(items, today)
        self.assertEqual(result, [("banana", "2025-01-01")])

    def test_all_expired(self):
        items = [("a", "2020-01-01"), ("b", "2021-06-15")]
        today = "2024-01-01"
        result = remove_expired_items(items, today)
        self.assertEqual(result, [])

    def test_none_expired(self):
        items = [("a", "2030-01-01"), ("b", "2035-12-31")]
        today = "2024-01-01"
        result = remove_expired_items(items, today)
        self.assertEqual(result, items)

    def test_empty_list(self):
        items = []
        today = "2024-01-01"
        result = remove_expired_items(items, today)
        self.assertEqual(result, [])

    def test_expiry_today(self):
        items = [("a", "2024-01-01")]
        today = "2024-01-01"
        result = remove_expired_items(items, today)
        self.assertEqual(result, [])

    def test_mixed_recent_and_expired(self):
        items = [("milk", "2024-01-15"), ("eggs", "2024-02-01"), ("bread", "2023-12-01")]
        today = "2024-01-20"
        result = remove_expired_items(items, today)
        self.assertEqual(result, [("eggs", "2024-02-01")])


if __name__ == "__main__":
    unittest.main()