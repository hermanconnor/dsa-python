class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        Time Complexity: O(1) amortized
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        Time Complexity: O(1)
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")

        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Time Complexity: O(1)
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        Time Complexity: O(1)
        """
        return len(self._items) == 0

    def clear(self):
        """
        Remove all items from the stack.
        Time Complexity: O(1)
        """
        self._items = []

    def __len__(self):
        """
        Allows using the len() function to get the size of the stack.
        """
        return len(self._items)

    def __str__(self):
        """
        Provides a user-friendly string representation of the stack.
        """
        return f"Top -> {self._items[::-1]}"

    def __repr__(self):
        """
        Provides a string representation of the stack.
        """
        return f"Stack({self._items})"
