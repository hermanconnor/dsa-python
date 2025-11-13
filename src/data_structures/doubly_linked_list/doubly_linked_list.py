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

    def insert(self, index: int, data: T) -> None:
        """
        Insert a new node at the specified index.
        Time complexity: O(n).
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        if index == self._size:
            self.append(data)
            return

        current = self._get_node(index)
        new_node = DoublyNode(data)

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

        self._size += 1

    def get(self, index: int) -> T:
        """
        Get the data at a specified index. (Used internally by __getitem__)
        Time complexity: O(n).
        """
        return self._get_node(index).data

    def get_head(self) -> T:
        """
        Return the data of the head node.
        Time complexity: O(1).
        """
        if not self.head:
            raise IndexError("List is empty")

        return self.head.data

    def get_tail(self) -> T:
        """
        Return the data of the tail node.
        Time complexity: O(1).
        """
        if not self.tail:
            raise IndexError("List is empty")

        return self.tail.data

    def _get_node(self, index: int) -> DoublyNode[T]:
        """
        Return the node at the specified index.
        Time complexity: O(n) in the worst case (O(n/2) average).
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current: Optional[DoublyNode[T]] = None

        # Traverse from the closest end for efficiency
        if index <= self._size // 2:
            current = self.head
            for _ in range(index):
                if current is None:
                    break  # Safety break, should not be reached
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - index - 1):
                if current is None:
                    break  # Safety break, should not be reached
                current = current.prev

        # This check is mainly to satisfy type-checkers (like mypy)
        if current is None:
            raise RuntimeError(
                "Internal list error: Node not found where expected.")

        return current

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
        return self.get(index)

    def __setitem__(self, index: int, data: T) -> None:
        """Support for list[index] = data assignment. O(n)."""
        pass

    def __delitem__(self, index: int) -> None:
        """Support for del list[index]. O(n)."""
        pass

    def __reversed__(self) -> Iterator[T]:
        """Reverse iterator. O(n) total to iterate through all nodes."""
        pass
