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

    def test_insert_in_middle(self):
        """Test inserting in the middle of the array."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(1, 2)

        assert len(arr) == 3
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3

    def test_insert_at_end(self):
        """Test inserting at the end of the array."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.insert(2, 3)

        assert len(arr) == 3
        assert arr[2] == 3

    def test_insert_out_of_bounds(self):
        """Test that inserting at invalid index raises IndexError."""
        arr = DynamicArray()
        arr.append(1)

        with pytest.raises(IndexError):
            arr.insert(5, 99)

        with pytest.raises(IndexError):
            arr.insert(-1, 99)

    def test_delete_by_index(self):
        """Test deleting element by index."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        deleted = arr.delete(1)

        assert deleted == 2
        assert len(arr) == 2
        assert arr[0] == 1
        assert arr[1] == 3

    def test_delete_negative_index(self):
        """Test deleting using negative index."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        deleted = arr.delete(-1)

        assert deleted == 3
        assert len(arr) == 2

    def test_delete_out_of_bounds(self):
        """Test that deleting at invalid index raises IndexError."""
        arr = DynamicArray()
        arr.append(1)

        with pytest.raises(IndexError):
            arr.delete(5)

    def test_delete_triggers_shrink(self):
        """Test that array shrinks when size drops below 1/4 capacity."""
        arr = DynamicArray()

        for i in range(10):
            arr.append(i)

        capacity_before = arr.capacity()

        for _ in range(8):
            arr.delete(0)

        assert arr.capacity() < capacity_before
