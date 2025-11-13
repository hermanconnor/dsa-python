from __future__ import annotations
from typing import Optional, Iterator, Generic, TypeVar, List

T = TypeVar('T')


class DoublyNode:
    """A node in a doubly linked list."""

    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional[DoublyNode[T]] = None
        self.next: Optional[DoublyNode[T]] = None

    def __repr__(self) -> str:
        return f"DoublyNode({self.data!r})"


class DoublyLinkedList(Generic[T]):
    """
    A doubly linked list implementation.
    """

    def __init__(self):
        self.head: Optional[DoublyNode[T]] = None
        self.tail: Optional[DoublyNode[T]] = None
        self._size: int = 0

    def append(self, data: T) -> None:
        """
        Add a new node at the end of the list.
        Time complexity: O(1).
        """
        new_node = DoublyNode(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, data: T) -> None:
        """
        Add a new node at the beginning of the list.
        Time complexity: O(1).
        """
        new_node = DoublyNode(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._size += 1

    def _get_node(self, index: int) -> DoublyNode[T]:
        """
        Return the node at the specified index.
        Time complexity: O(n) in the worst case (O(n/2) average).
        """
        pass

    def __len__(self) -> int:
        """Support for len(). O(1)."""
        return self._size

    def __str__(self) -> str:
        """Readable string representation. O(n)."""
        pass

    def __repr__(self) -> str:
        """Official string representation of the doubly linked list object, useful for debugging. O(n)."""
        pass

    def __iter__(self) -> Iterator[T]:
        """Forward iterator. O(n) total to iterate through all nodes."""
        current = self.head

        while current:
            yield current.data
            current = current.next

    def __contains__(self, data: T) -> bool:
        """Support for 'in' operator (data in list). O(n)."""
        pass

    def __getitem__(self, index: int) -> T:
        """Support for list[index] access. O(n)."""
        pass

    def __setitem__(self, index: int, data: T) -> None:
        """Support for list[index] = data assignment. O(n)."""
        pass

    def __delitem__(self, index: int) -> None:
        """Support for del list[index]. O(n)."""
        pass

    def __reversed__(self) -> Iterator[T]:
        """Reverse iterator. O(n) total to iterate through all nodes."""
        pass
