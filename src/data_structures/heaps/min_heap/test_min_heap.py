import pytest
from min_heap import MinHeap


class TestMinHeapBasics:
    """Test basic heap operations."""

    def test_initialization(self):
        """Test heap initialization."""
        heap = MinHeap[int]()

        assert len(heap) == 0
        assert not heap

    def test_peek_empty_heap(self):
        """Test peeking at an empty heap raises error."""
        heap = MinHeap[int]()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.peek()

    def test_extract_min_empty_heap(self):
        """Test extracting from an empty heap raises error."""
        heap = MinHeap[int]()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.extract_min()

    def test_replace_empty_heap(self):
        """Test replace on an empty heap raises error."""
        heap = MinHeap[int]()

        with pytest.raises(IndexError, match="Heap is empty"):
            heap.replace(5)


class TestMinHeapInsertionAndExtraction:
    """Test insertion and extraction operations."""

    def test_single_insert(self):
        """Test inserting a single element."""
        heap = MinHeap[int]()

        heap.insert(5)

        assert len(heap) == 1
        assert heap.peek() == 5

    def test_multiple_inserts_ascending(self):
        """Test inserting elements in ascending order."""
        heap = MinHeap[int]()

        values = [1, 2, 3, 4, 5]
        for val in values:
            heap.insert(val)

        assert len(heap) == 5
        assert heap.peek() == 1

    def test_multiple_inserts_descending(self):
        """Test inserting elements in descending order."""
        heap = MinHeap[int]()

        values = [5, 4, 3, 2, 1]
        for val in values:
            heap.insert(val)

        assert len(heap) == 5
        assert heap.peek() == 1

    def test_multiple_inserts_random(self):
        """Test inserting elements in random order."""
        heap = MinHeap[int]()

        values = [3, 7, 1, 9, 2, 5, 8]
        for val in values:
            heap.insert(val)

        assert len(heap) == 7
        assert heap.peek() == 1

    def test_extract_min_maintains_order(self):
        """Test that extract_min returns elements in sorted order."""
        heap = MinHeap[int]()

        values = [5, 3, 7, 1, 9, 2, 8, 4, 6]
        for val in values:
            heap.insert(val)

        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert extracted == sorted(values)
        assert len(heap) == 0

    def test_insert_duplicate_values(self):
        """Test inserting duplicate values."""
        heap = MinHeap[int]()

        values = [5, 3, 5, 1, 3, 1]
        for val in values:
            heap.insert(val)

        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert extracted == sorted(values)

    def test_insert_negative_numbers(self):
        """Test inserting negative numbers."""
        heap = MinHeap[int]()

        values = [5, -3, 0, -10, 7, -1]
        for val in values:
            heap.insert(val)

        assert heap.peek() == -10
        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert extracted == sorted(values)


class TestMinHeapBuildHeap:
    """Test building heap from array."""

    def test_build_heap_empty_array(self):
        """Test building heap from empty array."""
        heap = MinHeap[int]()

        heap.build_heap([])

        assert len(heap) == 0

    def test_build_heap_single_element(self):
        """Test building heap from single element."""
        heap = MinHeap[int]()

        heap.build_heap([5])

        assert len(heap) == 1
        assert heap.peek() == 5

    def test_build_heap_multiple_elements(self):
        """Test building heap from multiple elements."""
        heap = MinHeap[int]()

        values = [8, 4, 6, 2, 9, 1, 7, 3, 5]
        heap.build_heap(values)

        assert len(heap) == 9
        assert heap.peek() == 1

        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert extracted == sorted(values)

    def test_build_heap_does_not_modify_original(self):
        """Test that build_heap doesn't modify the original array."""
        heap = MinHeap[int]()

        original = [5, 3, 7, 1, 9]
        original_copy = original.copy()
        heap.build_heap(original)

        assert original == original_copy


class TestMinHeapReplace:
    """Test replace operation."""

    def test_replace_single_element(self):
        """Test replace with single element."""
        heap = MinHeap[int]()

        heap.insert(5)
        min_val = heap.replace(3)

        assert min_val == 5
        assert heap.peek() == 3
        assert len(heap) == 1

    def test_replace_maintains_heap_property(self):
        """Test that replace maintains min-heap property."""
        heap = MinHeap[int]()

        values = [5, 3, 7, 1, 9, 2]
        for val in values:
            heap.insert(val)

        min_val = heap.replace(4)
        assert min_val == 1

        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert extracted == sorted([2, 3, 4, 5, 7, 9])

    def test_replace_with_smaller_value(self):
        """Test replace with a smaller value than current min."""
        heap = MinHeap[int]()

        for val in [5, 3, 7]:
            heap.insert(val)

        min_val = heap.replace(1)
        assert min_val == 3
        assert heap.peek() == 1


class TestMinHeapMagicMethods:
    """Test magic methods."""

    def test_len(self):
        """Test __len__ method."""
        heap = MinHeap[int]()

        assert len(heap) == 0

        heap.insert(5)
        assert len(heap) == 1

        heap.insert(3)
        assert len(heap) == 2

        heap.extract_min()
        assert len(heap) == 1

    def test_bool(self):
        """Test __bool__ method."""
        heap = MinHeap[int]()
        assert not heap

        heap.insert(5)
        assert heap

        heap.extract_min()
        assert not heap

    def test_iter(self):
        """Test __iter__ method."""
        heap = MinHeap[int]()

        values = [5, 3, 7, 1, 9]
        for val in values:
            heap.insert(val)

        # Note: iteration order is not sorted, just the internal array
        heap_list = list(heap)
        assert len(heap_list) == 5
        assert set(heap_list) == set(values)

    def test_str(self):
        """Test __str__ method."""
        heap = MinHeap[int]()

        heap.insert(5)
        heap.insert(3)

        str_repr = str(heap)

        assert isinstance(str_repr, str)
        assert "3" in str_repr
        assert "5" in str_repr

    def test_repr(self):
        """Test __repr__ method."""
        heap = MinHeap[int]()

        heap.insert(5)
        heap.insert(3)

        repr_str = repr(heap)

        assert repr_str.startswith("MinHeap(")
        assert repr_str.endswith(")")


class TestMinHeapWithCustomKey:
    """Test heap with custom key function."""

    def test_tuple_with_key_function(self):
        """Test heap with tuples using key function."""
        heap = MinHeap[tuple](key=lambda x: x[1])

        tasks = [("Task A", 3), ("Task B", 1), ("Task C", 2)]

        for task in tasks:
            heap.insert(task)

        assert heap.peek() == ("Task B", 1)
        assert heap.extract_min() == ("Task B", 1)
        assert heap.extract_min() == ("Task C", 2)
        assert heap.extract_min() == ("Task A", 3)

    def test_custom_object_with_key_function(self):
        """Test heap with custom objects using key function."""
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

            def __eq__(self, other):
                return self.name == other.name and self.age == other.age

        heap = MinHeap[Person](key=lambda p: p.age)
        people = [
            Person("Alice", 30),
            Person("Bob", 25),
            Person("Charlie", 35)
        ]

        for person in people:
            heap.insert(person)

        youngest = heap.extract_min()
        assert youngest.name == "Bob"
        assert youngest.age == 25

    def test_string_length_key(self):
        """Test heap with strings sorted by length."""
        heap = MinHeap[str](key=lambda s: len(s))
        words = ["hello", "hi", "world", "a", "test"]

        for word in words:
            heap.insert(word)

        assert heap.peek() == "a"
        extracted = []
        while heap:
            extracted.append(heap.extract_min())

        assert [len(w) for w in extracted] == sorted([len(w) for w in words])


class TestMinHeapEdgeCases:
    """Test edge cases and corner cases."""

    def test_large_heap(self):
        """Test heap with large number of elements."""
        heap = MinHeap[int]()

        values = list(range(1000, 0, -1))

        for val in values:
            heap.insert(val)

        assert len(heap) == 1000
        assert heap.peek() == 1

        # Extract first 10 elements
        for i in range(1, 11):
            assert heap.extract_min() == i

    def test_alternating_insert_extract(self):
        """Test alternating insert and extract operations."""
        heap = MinHeap[int]()

        heap.insert(5)
        heap.insert(3)

        assert heap.extract_min() == 3

        heap.insert(7)
        heap.insert(1)

        assert heap.extract_min() == 1
        assert heap.extract_min() == 5
        assert heap.extract_min() == 7

    def test_insert_after_empty(self):
        """Test inserting after heap becomes empty."""
        heap = MinHeap[int]()

        heap.insert(5)
        heap.extract_min()

        heap.insert(3)
        assert heap.peek() == 3

    def test_build_heap_then_insert(self):
        """Test building heap then inserting more elements."""
        heap = MinHeap[int]()

        heap.build_heap([5, 3, 7])

        heap.insert(1)
        heap.insert(9)

        assert heap.peek() == 1
        assert len(heap) == 5

    def test_all_same_values(self):
        """Test heap with all identical values."""
        heap = MinHeap[int]()
        for _ in range(5):
            heap.insert(7)

        assert heap.peek() == 7
        for _ in range(5):
            assert heap.extract_min() == 7


class TestMinHeapProperties:
    """Test heap properties are maintained."""

    def test_heap_property_after_inserts(self):
        """Verify min-heap property is maintained after inserts."""
        heap = MinHeap[int]()

        values = [5, 3, 7, 1, 9, 2, 8, 4, 6]
        for val in values:
            heap.insert(val)
            # After each insert, root should be minimum
            assert heap.peek() == min(heap.heap)

    def test_heap_property_after_extracts(self):
        """Verify min-heap property is maintained after extracts."""
        heap = MinHeap[int]()

        values = [5, 3, 7, 1, 9, 2, 8, 4, 6]
        for val in values:
            heap.insert(val)

        while len(heap) > 1:
            heap.extract_min()
            # After each extract, root should still be minimum
            assert heap.peek() == min(heap.heap)

    def test_heap_property_after_build(self):
        """Verify min-heap property after building heap."""
        heap = MinHeap[int]()

        heap.build_heap([8, 4, 6, 2, 9, 1, 7, 3, 5])

        # Root should be minimum
        assert heap.peek() == min(heap.heap)

        # Verify heap property for all nodes
        for i in range(len(heap.heap)):
            if heap.has_left_child(i):
                assert heap.heap[i] <= heap.heap[heap.left_child(i)]
            if heap.has_right_child(i):
                assert heap.heap[i] <= heap.heap[heap.right_child(i)]
