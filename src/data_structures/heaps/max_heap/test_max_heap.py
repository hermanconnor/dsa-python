import pytest
from max_heap import MaxHeap


class TestMaxHeapBasics:
    """Test basic heap operations."""

    def test_initialization(self):
        """Test heap initialization."""
        heap = MaxHeap()

        assert len(heap) == 0
        assert not heap
        assert str(heap) == "[]"

    def test_insert_and_peek(self):
        """Test inserting elements and peeking at max."""
        heap = MaxHeap()

        heap.insert(5)

        assert heap.peek() == 5
        assert len(heap) == 1

        heap.insert(10)
        assert heap.peek() == 10
        assert len(heap) == 2

        heap.insert(3)
        assert heap.peek() == 10
        assert len(heap) == 3

    def test_peek_empty_heap(self):
        """Test peeking at empty heap raises error."""
        heap = MaxHeap()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.peek()

    def test_extract_max(self):
        """Test extracting maximum elements."""
        heap = MaxHeap()

        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        heap.insert(8)

        assert heap.extract_max() == 10
        assert heap.extract_max() == 8
        assert heap.extract_max() == 5
        assert heap.extract_max() == 3
        assert len(heap) == 0

    def test_extract_max_empty_heap(self):
        """Test extracting from empty heap raises error."""
        heap = MaxHeap()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.extract_max()


class TestMaxHeapBuildHeap:
    """Test building heap from array."""

    def test_build_heap_from_array(self):
        """Test building heap from unsorted array."""
        heap = MaxHeap()

        heap.build_heap([3, 1, 4, 1, 5, 9, 2, 6])

        assert heap.peek() == 9
        result = []
        while heap:
            result.append(heap.extract_max())

        assert result == [9, 6, 5, 4, 3, 2, 1, 1]

    def test_build_heap_empty_array(self):
        """Test building heap from empty array."""
        heap = MaxHeap()

        heap.build_heap([])

        assert len(heap) == 0

    def test_build_heap_single_element(self):
        """Test building heap from single element."""
        heap = MaxHeap()

        heap.build_heap([42])

        assert heap.peek() == 42
        assert len(heap) == 1


class TestMaxHeapReplace:
    """Test replace operation."""

    def test_replace(self):
        """Test replacing root element."""
        heap = MaxHeap()

        heap.build_heap([10, 8, 6, 4, 2])

        old_max = heap.replace(7)

        assert old_max == 10
        assert heap.peek() == 8

    def test_replace_empty_heap(self):
        """Test replace on empty heap raises error."""
        heap = MaxHeap()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.replace(5)

    def test_replace_maintains_heap_property(self):
        """Test that replace maintains max heap property."""
        heap = MaxHeap()

        heap.build_heap([20, 15, 10, 8, 5])

        heap.replace(12)
        # Verify heap property by extracting all elements
        result = []
        while heap:
            result.append(heap.extract_max())

        # Should be sorted descending
        assert result == sorted(result, reverse=True)


class TestMaxHeapWithKeyFunction:
    """Test heap with custom key function."""

    def test_heap_with_tuple_key(self):
        """Test heap with tuples using second element as key."""
        heap = MaxHeap(key=lambda x: x[1])

        heap.insert(("apple", 5))
        heap.insert(("banana", 10))
        heap.insert(("cherry", 3))

        assert heap.peek() == ("banana", 10)
        assert heap.extract_max() == ("banana", 10)
        assert heap.extract_max() == ("apple", 5)
        assert heap.extract_max() == ("cherry", 3)

    def test_heap_with_object_key(self):
        """Test heap with custom objects."""
        class Task:
            def __init__(self, name, priority):
                self.name = name
                self.priority = priority

        heap = MaxHeap(key=lambda task: task.priority)

        heap.insert(Task("low", 1))
        heap.insert(Task("high", 10))
        heap.insert(Task("medium", 5))

        assert heap.peek().name == "high"
        assert heap.extract_max().priority == 10
        assert heap.extract_max().priority == 5
        assert heap.extract_max().priority == 1

    def test_heap_with_negative_numbers(self):
        """Test heap with negative numbers."""
        heap = MaxHeap()

        heap.build_heap([-5, -1, -10, -3, -7])

        assert heap.extract_max() == -1
        assert heap.extract_max() == -3
        assert heap.extract_max() == -5


class TestMaxHeapSpecialMethods:
    """Test special methods and properties."""

    def test_len(self):
        """Test __len__ method."""
        heap = MaxHeap()

        assert len(heap) == 0

        heap.insert(5)
        assert len(heap) == 1

        heap.insert(10)
        assert len(heap) == 2

        heap.extract_max()
        assert len(heap) == 1

    def test_bool(self):
        """Test __bool__ method."""
        heap = MaxHeap()

        assert not heap

        heap.insert(5)
        assert heap

        heap.extract_max()
        assert not heap

    def test_iter(self):
        """Test __iter__ method."""
        heap = MaxHeap()

        heap.build_heap([3, 1, 4, 1, 5])

        # Note: iteration order is not sorted
        elements = list(heap)
        assert len(elements) == 5
        assert set(elements) == {1, 3, 4, 5}

    def test_str_and_repr(self):
        """Test string representation."""
        heap = MaxHeap()

        heap.insert(5)
        heap.insert(10)

        str_repr = str(heap)
        assert "5" in str_repr
        assert "10" in str_repr

        repr_str = repr(heap)
        assert "MaxHeap" in repr_str


class TestMaxHeapEdgeCases:
    """Test edge cases and stress scenarios."""

    def test_large_heap(self):
        """Test heap with many elements."""
        heap = MaxHeap()
        n = 1000
        heap.build_heap(list(range(n)))

        # Extract first 10 and verify they're in order
        result = [heap.extract_max() for _ in range(10)]
        assert result == list(range(n - 1, n - 11, -1))

    def test_all_same_values(self):
        """Test heap with all identical values."""
        heap = MaxHeap()
        heap.build_heap([5, 5, 5, 5, 5])

        assert heap.extract_max() == 5
        assert heap.extract_max() == 5
        assert len(heap) == 3

    def test_already_sorted_ascending(self):
        """Test building heap from already sorted ascending array."""
        heap = MaxHeap()
        heap.build_heap([1, 2, 3, 4, 5])

        assert heap.extract_max() == 5
        assert heap.extract_max() == 4
        assert heap.extract_max() == 3

    def test_already_sorted_descending(self):
        """Test building heap from already sorted descending array."""
        heap = MaxHeap()
        heap.build_heap([5, 4, 3, 2, 1])

        assert heap.extract_max() == 5
        assert heap.extract_max() == 4
        assert heap.extract_max() == 3

    def test_alternating_insert_extract(self):
        """Test alternating insertions and extractions."""
        heap = MaxHeap()

        heap.insert(5)
        heap.insert(10)
        assert heap.extract_max() == 10

        heap.insert(3)
        heap.insert(7)
        assert heap.extract_max() == 7

        heap.insert(15)
        assert heap.extract_max() == 15
        assert heap.extract_max() == 5
        assert heap.extract_max() == 3
