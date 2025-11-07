import ctypes


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def append(self, value):
        """
        Append an element to the end of the array.
        Amortized O(1) time complexity.

        Args:
            value: Element to append.
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._size] = value
        self._size += 1

    def insert(self, index, value):
        """
        Insert an element at the given index.
        O(n) time complexity.

        Args:
            index (int): Index where to insert the element.
            value: Element to insert.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds")

        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._A[i] = self._A[i - 1]

        self._A[index] = value
        self._size += 1

    def delete(self, index):
        """
        Delete element at the given index.
        O(n) time complexity.

        Args:
            index (int): Index of the element to delete.

        Returns:
            The deleted element.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not -self._size <= index < self._size:
            raise IndexError("Index out of bounds")

        if index < 0:
            index += self._size

        deleted_value = self._A[index]

        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._A[i] = self._A[i + 1]

        self._size -= 1

        # Shrink capacity if array is 1/4 full
        if self._size > 0 and self._size < self._capacity // 4:
            self._resize(self._capacity // 2)

        return deleted_value

    def remove(self, value):
        """
        Remove the first occurrence of a value from the array.
        O(n) time complexity.

        Args:
            value: Value to remove.

        Raises:
            ValueError: If value is not found.
        """
        for i in range(self._size):
            if self._A[i] == value:
                self.delete(i)
                return

        raise ValueError(f"{value} not in array")

    def pop(self, index=-1):
        """
        Remove and return element at the given index (default: last element).
        O(n) time complexity for arbitrary index, O(1) for last element.

        Args:
            index (int): Index of the element to remove (default: -1).

        Returns:
            The removed element.

        Raises:
            IndexError: If the array is empty or index is out of bounds.
        """
        if self._size == 0:
            raise IndexError("pop from empty array")

        return self.delete(index)

    def index(self, value):
        """
        Find the index of the first occurrence of a value.
        O(n) time complexity.

        Args:
            value: Value to search for.

        Returns:
            Index of the first occurrence.

        Raises:
            ValueError: If value is not found.
        """
        for i in range(self._size):
            if self._A[i] == value:
                return i

        raise ValueError(f"{value} not in array")

    def clear(self):
        """
        Remove all elements from the array.
        O(1) time complexity.
        """
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def is_empty(self):
        """Check if the array is empty."""
        return self._size == 0

    def capacity(self):
        """Return the current capacity of the array."""
        return self._capacity

    def _resize(self, new_capacity):
        """
        Resize the internal array to the new capacity.
        O(n) time complexity.

        Args:
            new_capacity (int): New capacity for the array.
        """
        new_array = self._make_array(new_capacity)

        for i in range(self._size):
            new_array[i] = self._A[i]

        self._A = new_array
        self._capacity = new_capacity

    def _make_array(self, new_capacity):
        """Return a new array with capacity, new_capacity."""
        return (ctypes.py_object * new_capacity)()

    def __getitem__(self, index):
        """
        Get element at the given index.

        Args:
            index (int): Index of the element to retrieve.

        Returns:
            The element at the given index.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not -self._size <= index < self._size:
            raise IndexError("Index out of bounds")

        if index < 0:
            index += self._size

        return self._A[index]

    def __setitem__(self, index, value):
        """
        Set element at the given index.

        Args:
            index (int): Index where to set the value.
            value: Value to set.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not -self._size <= index < self._size:
            raise IndexError("Index out of bounds")

        if index < 0:
            index += self._size

        self._A[index] = value

    def __len__(self):
        """Return the number of elements in the array."""
        return self._size

    def __str__(self):
        """Return string representation of the array."""
        return "[" + ", ".join(str(self._A[i]) for i in range(self._size)) + "]"

    def __repr__(self):
        """Return detailed representation of the array."""
        return f"DynamicArray({[self._A[i] for i in range(self._size)]})"
