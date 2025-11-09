from collections import Counter
from typing import Iterator, Hashable


class Multiset:
    """Multiset (Bag) implementation using Python's Counter class."""

    def __init__(self):
        self.items = Counter()
        self._size = 0

    def add(self, item: Hashable) -> None:
        """Add an item to the multiset - O(1) average."""
        self.items[item] += 1
        self._size += 1

    def remove(self, item: Hashable) -> bool:
        """
        Remove one occurrence of item.
        Returns True if the item was removed, False otherwise - O(1) average.
        """
        if self.items[item] > 0:
            self.items[item] -= 1
            self._size -= 1
            # Clean up the Counter if the count reaches zero
            if self.items[item] == 0:
                del self.items[item]

            return True

        return False

    def count(self, item: Hashable) -> int:
        """Count occurrences of item - O(1) average."""
        # Counter naturally returns 0 for non-existent items
        return self.items[item]

    def is_empty(self) -> bool:
        """Check if multiset is empty - O(1)"""
        return self._size == 0

    def __len__(self) -> int:
        """Returns total number of items - O(1)."""
        return self._size

    def __contains__(self, item: Hashable) -> bool:
        """Support 'in' operator (e.g., if 'apple' in bag) - O(1) average."""
        return self.items[item] > 0

    def __iter__(self) -> Iterator[Hashable]:
        """Make bag iterable, yielding all items including duplicates."""
        return self.items.elements()

    def __repr__(self) -> str:
        """
        Returns s string representation for debugging/console use.
        Shows the internal Counter contents.
        """
        return f"BagCounter({dict(self.items)})"
