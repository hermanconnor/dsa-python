from typing import TypeVar, Generic, List, Tuple, Optional

K = TypeVar('K')
V = TypeVar('V')


class HashMap(Generic[K, V]):
    def __init__(self, initial_capacity: int = 16) -> None:
        """
        Initialize hash map with given capacity.

        Time Complexity: O(n) where n is initial_capacity
        Space Complexity: O(n)
        """
        pass

    def _hash(self):
        pass

    def _resize(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    def remove(self):
        pass

    def contains(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
