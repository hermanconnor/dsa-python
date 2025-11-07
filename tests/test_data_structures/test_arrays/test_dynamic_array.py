from src.data_structures.arrays.dynamic_array import DynamicArray


class TestDynamicArrayInit:
    """Tests for initialization."""

    def test_default_initialization(self):
        arr = DynamicArray()
        assert len(arr) == 0
        assert arr.capacity() == 1
        assert arr.is_empty()
