from __future__ import annotations
from typing import TypeVar, Generic, Optional, Iterator, List

T = TypeVar("T")


class Node(Generic[T]):
    """A single node in the linked list."""

    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional[Node[T]] = None

    def __repr__(self) -> str:
        """Official string representation of a Node object."""
        return f"Node({self.data!r})"


class LinkedList(Generic[T]):
    """
    A singly linked list implementation with head and tail pointers.
    """

    def __init__(self) -> None:
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    def append(self, data: T) -> None:
        """Add a new node at the end of the list. O(1)."""
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def prepend(self, data: T) -> None:
        """Add a new node at the beginning of the list. O(1)."""
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def insert(self, index: int, data: T) -> None:
        """Insert a new node at the specified index. O(n)."""
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        if index == self._size:
            self.append(data)
            return

        new_node = Node(data)
        current = self._head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def pop_left(self) -> T:
        """Remove and return the data of the head node (first element). O(1)."""
        if self._head is None:
            raise IndexError("pop_left from empty list")

        data = self._head.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next

        self._size -= 1
        return data

    def pop(self) -> T:
        """Remove and return the data of the tail node (last element). O(n)."""
        if self._tail is None:
            raise IndexError("pop from empty list")

        data = self._tail.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current and current.next != self._tail:
                current = current.next

            current.next = None
            self._tail = current

        self._size -= 1
        return data

    def delete(self, data: T) -> bool:
        """Delete the first occurrence of data from the list. O(n)."""
        if self._head is None:
            return False

        if self._head.data == data:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._size -= 1
            return True

        current = self._head
        while current.next:
            if current.next.data == data:
                if current.next == self._tail:
                    self._tail = current
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def delete_at_index(self, index: int) -> T:
        """Delete the node at the specified index. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            return self.pop_left()

        current = self._head
        for _ in range(index - 1):
            current = current.next

        deleted_data = current.next.data

        if current.next == self._tail:
            self._tail = current

        current.next = current.next.next
        self._size -= 1
        return deleted_data

    def find(self, data: T) -> int:
        """Find the index of the first occurrence of data. O(n)."""
        for index, item_data in enumerate(self):
            if item_data == data:
                return index
        return -1

    def get(self, index: int) -> T:
        """Get the data at the specified index. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current = self._head
        for _ in range(index):
            current = current.next

        return current.data

    def get_head(self) -> T:
        """Get the data of the head node. O(1)."""
        if self._head is None:
            raise IndexError("List is empty")
        return self._head.data

    def get_tail(self) -> T:
        """Get the data of the tail node. O(1)."""
        if self._tail is None:
            raise IndexError("List is empty")
        return self._tail.data

    def is_empty(self) -> bool:
        """Check if the list is empty. O(1)."""
        return self._head is None

    def reverse(self) -> None:
        """Reverse the linked list in-place. O(n)."""
        if self._head is None or self._head.next is None:
            return

        prev: Optional[Node[T]] = None
        current: Optional[Node[T]] = self._head
        self._tail = self._head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self._head = prev

    def to_list(self) -> List[T]:
        """Convert the linked list to a Python list. O(n)."""
        result: List[T] = []
        current = self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self) -> int:
        """Support for the len() function."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over the linked list. O(n) total."""
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """String representation for print() in a list-like format. O(n)."""
        elements = [str(data) for data in self]
        return f"[{', '.join(elements)}]"

    def __repr__(self) -> str:
        """Official string representation of the list object, useful for debugging. O(n)."""
        elements: List[str] = []
        current = self._head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return f"LinkedList([{', '.join(elements)}])"
