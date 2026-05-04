from collections import Counter
from typing import Any, Iterable, Iterator, Hashable


class Multiset:
    """Multiset (Bag) implementation using Python's Counter class."""

    def __init__(self, iterable: Iterable[Hashable] = None) -> None:
        self.items = Counter()
        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.add(item)

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

    def clear(self) -> None:
        """Remove all items from the multiset - O(1)"""
        self.items.clear()
        self._size = 0

    def distinct_elements(self) -> None:
        """Return a set of all unique items in the multiset."""
        return set(self.items.keys())

    def __len__(self) -> int:
        """Returns total number of items - O(1)."""
        return self._size

    def __contains__(self, item: Hashable) -> bool:
        """Support 'in' operator (e.g., if 'apple' in bag) - O(1) average."""
        return item in self.items

    def __iter__(self) -> Iterator[Hashable]:
        """Make bag iterable, yielding all items including duplicates."""
        return self.items.elements()

    def __eq__(self, other: Any) -> bool:
        """Check if two multisets are equal."""
        if not isinstance(other, Multiset):
            return NotImplemented

        return self.items == other.items

    def __add__(self, other: "Multiset") -> "Multiset":
        """Disjoint Union: sum counts of elements from both multisets."""
        if not isinstance(other, Multiset):
            return NotImplemented

        result = Multiset()
        result.items = self.items + other.items
        result._size = self._size + other._size

        return result

    def __sub__(self, other: "Multiset") -> "Multiset":
        """Difference: subtract counts of elements, keeping only positives."""
        if not isinstance(other, Multiset):
            return NotImplemented

        result = Multiset()
        result.items = self.items - other.items
        result._size = sum(result.items.values())

        return result

    def __and__(self, other: "Multiset") -> "Multiset":
        """Intersection: keeps the minimum count of matching elements."""
        if not isinstance(other, Multiset):
            return NotImplemented

        result = Multiset()
        result.items = self.items & other.items
        result._size = sum(result.items.values())

        return result

    def __or__(self, other: "Multiset") -> "Multiset":
        """Union: keeps the maximum count of matching elements."""
        if not isinstance(other, Multiset):
            return NotImplemented

        result = Multiset()
        result.items = self.items | other.items
        result._size = sum(result.items.values())

        return result

    def __repr__(self) -> str:
        """Returns s string representation for debugging/console use."""
        return f"Multiset({dict(self.items)})"
