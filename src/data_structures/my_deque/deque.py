from __future__ import annotations
from typing import Generic, TypeVar, Optional, Iterator

T = TypeVar('T')


class Node(Generic[T]):
    """Node for a doubly linked list used in Deque."""

    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None

    def __repr__(self) -> str:
        """Official string representation of a Node object."""
        return f"Node({self.data!r})"


class Deque(Generic[T]):
    """Deque (double-ended queue) implemented using a doubly linked list."""

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size: int = 0

    def appendleft(self, item: T) -> None:
        """Add an item to the front of the deque. O(1)"""
        pass

    def append(self, item: T) -> None:
        """Add an item to the rear of the deque. O(1)"""
        pass

    def popleft(self) -> T:
        """Remove and return the front item from the deque. O(1)
        Raises:
            IndexError: If the deque is empty.
        """
        pass

    def pop(self) -> T:
        """Remove and return the rear item from the deque. O(1)
        Raises:
            IndexError: If the deque is empty.
        """
        pass

    def peek_front(self) -> T:
        """Return the front item without removing it. O(1)
        Raises:
            IndexError: If the deque is empty.
        """
        pass

    def peek_rear(self) -> T:
        """Return the rear item without removing it. O(1)
        Raises:
            IndexError: If the deque is empty.
        """
        pass

    def is_empty(self) -> bool:
        """Check whether the deque is empty. O(1)"""
        pass

    def clear(self) -> None:
        """Remove all elements from the deque. O(1)"""
        pass

    def __len__(self) -> int:
        """Return the number of elements in the deque. O(1)"""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Iterate over elements from front to rear. O(n)"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __reversed__(self) -> Iterator[T]:
        """Iterate over elements from rear to front. O(n)"""
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    def __contains__(self, item: T) -> bool:
        """Check if an item exists in the deque. O(n)"""
        return any(element == item for element in self)

    def __getitem__(self, index: int) -> T:
        """Return the item at a given position. O(n)
        Supports negative indexing.
        Raises:
            IndexError: If index is out of range.
        """
        if not -self._size <= index < self._size:
            raise IndexError("deque index out of range")

        # Normalize negative indices
        if index < 0:
            index += self._size

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def __eq__(self, other: object) -> bool:
        """Check equality with another deque. O(n)"""
        if not isinstance(other, Deque):
            return False
        return list(self) == list(other)

    def __str__(self) -> str:
        """Return a string representation of the deque. O(n)"""
        return f"Deque([{', '.join(map(str, self))}])"

    def __repr__(self) -> str:
        """Return a string representation of the deque. O(n)"""
        return str(self)
