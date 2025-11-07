import ctypes


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def append(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def delete(self):
        pass

    def pop(self):
        pass

    def index(self):
        pass

    def clear(self):
        pass

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
        return (new_capacity * ctypes.py_object)()

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
