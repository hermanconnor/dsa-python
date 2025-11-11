class Node:
    """A single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Official string representation of a Node object."""
        return f"Node({repr(self.data)})"


class LinkedList:
    """
    A singly linked list implementation with head and tail pointers.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self):
        pass

    def prepend(self):
        pass

    def insert(self):
        pass

    def pop_left(self):
        pass

    def pop(self):
        pass

    def delete(self):
        pass

    def delete_at_index(self):
        pass

    def find(self):
        pass

    def get(self):
        pass

    def get_head(self):
        pass

    def get_tail(self):
        pass

    def is_empty(self):
        pass

    def reverse(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
