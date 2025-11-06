import ctypes


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, new_capacity):
        """Return a new array with capacity, new_capacity."""
        return (new_capacity * ctypes.py_object)()

    def __len__(self):
        """Return the number of elements in the array."""
        return self._size

    def __str__(self):
        """Return string representation of the array."""
        return "[" + ", ".join(str(self._A[i]) for i in range(self._size)) + "]"

    def __repr__(self):
        """Return detailed representation of the array."""
        return f"DynamicArray({[self._A[i] for i in range(self._size)]})"
