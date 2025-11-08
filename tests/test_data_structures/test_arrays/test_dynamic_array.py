import pytest
from src.data_structures.arrays.dynamic_array import DynamicArray


class TestDynamicArray:
    """Test suite for DynamicArray class."""

    def test_default_initialization(self):
        arr = DynamicArray()
        assert len(arr) == 0
        assert arr.capacity() == 1
        assert arr.is_empty()

    def test_append(self):
        """Test appending elements to the array."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        assert len(arr) == 3
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3

    def test_append_resize(self):
        """Test that array resizes when capacity is exceeded."""
        arr = DynamicArray()
        initial_capacity = arr.capacity()

        for i in range(10):
            arr.append(i)

        assert len(arr) == 10
        assert arr.capacity() > initial_capacity

    def test_insert_at_beginning(self):
        """Test inserting at the beginning of the array."""
        arr = DynamicArray()
        arr.append(2)
        arr.append(3)
        arr.insert(0, 1)

        assert len(arr) == 3
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3
