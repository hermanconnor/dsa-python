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

    def append(self, data):
        """Add a new node at the end of the list. O(1)."""
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def prepend(self, data):
        """Add a new node at the beginning of the list. O(1)."""
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def insert(self, index, data):
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

        # Stop at the node BEFORE the insertion point
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self._size += 1

    def pop_left(self):
        """Remove and return the data of the head node (first element). O(1)."""
        if self._head is None:
            raise IndexError("pop_left from empty list")

        data = self._head.data

        if self._head == self._tail:  # Only one element
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next

        self._size -= 1
        return data

    def pop(self):
        """Remove and return the data of the tail node (last element). O(n) for Singly List."""
        if self._tail is None:
            raise IndexError("pop from empty list")

        data = self._tail.data

        if self._head == self._tail:  # Only one element
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.next != self._tail:
                current = current.next

            current.next = None
            self._tail = current

        self._size -= 1
        return data

    def delete(self, data):
        """Delete the first occurrence of data from the list. O(n)."""
        if self._head is None:
            return False

        # Case 1: Deleting the head node
        if self._head.data == data:
            self._head = self._head.next
            if self._head is None:  # If list is now empty
                self._tail = None
            self._size -= 1
            return True

        current = self._head
        while current.next:
            if current.next.data == data:
                # Case 2: Deleting the tail node
                if current.next == self._tail:
                    self._tail = current

                # Delete the node
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

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
