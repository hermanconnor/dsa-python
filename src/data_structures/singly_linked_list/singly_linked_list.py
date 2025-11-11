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
        """Support for the len() function."""
        return self._size

    def __iter__(self):
        """
        Allow iteration over the linked list (yields nodes). O(n) total.
        Example: for node in my_list: print(node.data)
        """
        current = self._head
        while current:
            yield current.data  # Yield the data for general list-like use
            current = current.next

    def __str__(self):
        """String representation for print() in a list-like format. O(n)."""
        elements = [str(data) for data in self]
        return f"[{', '.join(elements)}]"

    def __repr__(self):
        """Official string representation of the list object, useful for debugging. O(n)."""
        elements = []
        current = self._head

        while current:
            elements.append(repr(current.data))
            current = current.next

        return f"LinkedList([{', '.join(elements)}])"
