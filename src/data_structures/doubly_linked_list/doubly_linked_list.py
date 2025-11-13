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

    def delete(self, data: T) -> bool:
        """
        Delete the first occurrence of a value from the list.
        Returns True if deleted, False if not found.
        Time complexity: O(n).
        """
        current = self.head
        while current:
            if current.data == data:
                self._remove_node(current)
                return True

            current = current.next

        return False

    def delete_at_index(self, index: int) -> T:
        """
        Delete the node at the specified index and return its data.
        Time complexity: O(n).
        """
        node = self._get_node(index)
        return self._remove_node(node)

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

    def find(self, data: T) -> int:
        """
        Find the index of the first occurrence of data.
        Returns -1 if not found.
        Time complexity: O(n).
        """
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def find_from_tail(self, data: T) -> int:
        """
        Find the index of the last occurrence of data by searching from tail.
        Returns -1 if not found.
        Time complexity: O(n).
        """
        current = self.tail
        index = self._size - 1

        while current:
            if current.data == data:
                return index
            current = current.prev
            index -= 1

        return -1

    def reverse(self) -> None:
        """
        Reverse the list in-place.
        Time complexity: O(n).
        """
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def clear(self) -> None:
        """
        Remove all nodes from the list.
        Time complexity: O(1).
        """
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Check if the list is empty.
        Time complexity: O(1).
        """
        return self._size == 0

    def to_list_forward(self) -> List[T]:
        """
        Convert the list to a standard Python list (head → tail).
        Time complexity: O(n).
        """
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def to_list_backward(self) -> List[T]:
        """
        Convert the list to a standard Python list (tail → head).
        Time complexity: O(n).
        """
        result = []
        current = self.tail

        while current:
            result.append(current.data)
            current = current.prev

        return result

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

    def _remove_node(self, node: DoublyNode[T]) -> T:
        """
        Helper to unlink and remove a node from the list.
        Time complexity: O(1).
        """
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self._size -= 1
        return node.data

    def __len__(self) -> int:
        """Support for len(). O(1)."""
        return self._size

    def __str__(self) -> str:
        """Readable string representation. O(n)."""
        return f"[{', '.join(map(str, self.to_list_forward()))}]"

    def __repr__(self) -> str:
        """Official string representation of the doubly linked list object, useful for debugging. O(n)."""
        return f"DoublyLinkedList([{', '.join(map(repr, self.to_list_forward()))}])"

    def __iter__(self) -> Iterator[T]:
        """Forward iterator. O(n) total to iterate through all nodes."""
        current = self.head

        while current:
            yield current.data
            current = current.next

    def __contains__(self, data: T) -> bool:
        """Support for 'in' operator (data in list). O(n)."""
        return self.find(data) != -1

    def __getitem__(self, index: int) -> T:
        """Support for list[index] access. O(n)."""
        return self.get(index)

    def __setitem__(self, index: int, data: T) -> None:
        """Support for list[index] = data assignment. O(n)."""
        node = self._get_node(index)
        node.data = data

    def __delitem__(self, index: int) -> None:
        """Support for del list[index]. O(n)."""
        self.delete_at_index(index)

    def __reversed__(self) -> Iterator[T]:
        """Reverse iterator. O(n) total to iterate through all nodes."""
        current = self.tail

        while current:
            yield current.data
            current = current.prev
