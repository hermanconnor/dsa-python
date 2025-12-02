import pytest
from hashset import HashSet


class TestHashSetBasics:
    """Test basic HashSet operations"""

    def test_initialization(self):
        """Test that HashSet initializes correctly"""
        hs = HashSet[int]()

        assert len(hs) == 0
        assert hs.capacity == 16

    def test_initialization_custom_capacity(self):
        """Test initialization with custom capacity"""
        hs = HashSet[int](initial_capacity=32)

        assert len(hs) == 0
        assert hs.capacity == 32

    def test_add_single_element(self):
        """Test adding a single element"""
        hs = HashSet[int]()

        result = hs.add(5)

        assert result is True
        assert len(hs) == 1
        assert 5 in hs

    def test_add_duplicate(self):
        """Test that adding duplicate returns False"""
        hs = HashSet[int]()

        hs.add(5)
        result = hs.add(5)

        assert result is False
        assert len(hs) == 1

    def test_add_multiple_elements(self):
        """Test adding multiple elements"""
        hs = HashSet[int]()

        for i in range(10):
            hs.add(i)
        assert len(hs) == 10
        for i in range(10):
            assert i in hs


class TestHashSetIteration:
    """Test iteration capabilities"""

    def test_iteration(self):
        """Test that set can be iterated"""
        hs = HashSet[int]()

        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            hs.add(elem)

        iterated = list(hs)

        assert len(iterated) == 5
        assert set(iterated) == set(elements)

    def test_iteration_empty(self):
        """Test iterating empty set"""
        hs = HashSet[int]()

        iterated = list(hs)

        assert len(iterated) == 0


class TestHashSetStringRepresentation:
    """Test string representations"""

    def test_str(self):
        """Test __str__ method"""
        hs = HashSet[int]()

        hs.add(1)
        hs.add(2)
        result = str(hs)

        assert result.startswith("{")
        assert result.endswith("}")
        assert "1" in result
        assert "2" in result

    def test_repr(self):
        """Test __repr__ method"""
        hs = HashSet[int]()

        hs.add(1)
        result = repr(hs)

        assert "HashSet" in result
        assert "size=1" in result
        assert "capacity=" in result


class TestHashSetMembership:
    """Test membership operations"""

    def test_contains_existing(self):
        """Test contains with existing element"""
        hs = HashSet[str]()

        hs.add("hello")

        assert hs.contains("hello")
        assert "hello" in hs

    def test_contains_nonexistent(self):
        """Test contains with non-existent element"""
        hs = HashSet[str]()

        hs.add("hello")

        assert not hs.contains("world")
        assert "world" not in hs

    def test_contains_after_removal(self):
        """Test contains after element removal"""
        hs = HashSet[int]()

        hs.add(42)
        hs.remove(42)

        assert not hs.contains(42)


class TestHashSetRemoval:
    """Test removal operations"""

    def test_remove_existing(self):
        """Test removing an existing element"""
        hs = HashSet[int]()

        hs.add(10)
        result = hs.remove(10)

        assert result is True
        assert len(hs) == 0
        assert 10 not in hs

    def test_remove_nonexistent(self):
        """Test removing a non-existent element"""
        hs = HashSet[int]()

        result = hs.remove(10)

        assert result is False
        assert len(hs) == 0

    def test_remove_multiple(self):
        """Test removing multiple elements"""
        hs = HashSet[int]()

        for i in range(5):
            hs.add(i)

        hs.remove(2)
        hs.remove(4)

        assert len(hs) == 3
        assert 0 in hs
        assert 1 in hs
        assert 3 in hs
        assert 2 not in hs
        assert 4 not in hs


class TestHashSetClear:
    """Test clear operation"""

    def test_clear_empty(self):
        """Test clearing an empty set"""
        hs = HashSet[int]()

        hs.clear()
        assert len(hs) == 0

    def test_clear_with_elements(self):
        """Test clearing a set with elements"""
        hs = HashSet[int]()

        for i in range(10):
            hs.add(i)

        hs.clear()

        assert len(hs) == 0
        for i in range(10):
            assert i not in hs


class TestHashSetResize:
    """Test automatic resizing"""

    def test_resize_occurs(self):
        """Test that resize happens when load factor exceeded"""
        hs = HashSet[int](initial_capacity=4)

        initial_capacity = hs.capacity

        # Add enough elements to trigger resize (load factor = 0.75)
        for i in range(10):
            hs.add(i)

        assert hs.capacity > initial_capacity
        assert len(hs) == 10

        # Verify all elements still accessible
        for i in range(10):
            assert i in hs

    def test_elements_preserved_after_resize(self):
        """Test that all elements are preserved after resize"""
        hs = HashSet[str](initial_capacity=2)

        elements = ["a", "b", "c", "d", "e", "f"]

        for elem in elements:
            hs.add(elem)

        for elem in elements:
            assert elem in hs


class TestHashSetUnion:
    """Test union operation"""

    def test_union_disjoint(self):
        """Test union of disjoint sets"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in range(5):
            set1.add(i)
        for i in range(5, 10):
            set2.add(i)

        result = set1.union(set2)

        assert len(result) == 10
        for i in range(10):
            assert i in result

    def test_union_overlapping(self):
        """Test union of overlapping sets"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3, 4]:
            set1.add(i)
        for i in [3, 4, 5, 6]:
            set2.add(i)

        result = set1.union(set2)

        assert len(result) == 6
        for i in [1, 2, 3, 4, 5, 6]:
            assert i in result

    def test_union_empty(self):
        """Test union with empty set"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        set1.add(1)
        set1.add(2)

        result = set1.union(set2)

        assert len(result) == 2
        assert 1 in result
        assert 2 in result


class TestHashSetIntersection:
    """Test intersection operation"""

    def test_intersection_common_elements(self):
        """Test intersection with common elements"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3, 4]:
            set1.add(i)
        for i in [3, 4, 5, 6]:
            set2.add(i)

        result = set1.intersection(set2)

        assert len(result) == 2
        assert 3 in result
        assert 4 in result

    def test_intersection_disjoint(self):
        """Test intersection of disjoint sets"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in range(5):
            set1.add(i)
        for i in range(5, 10):
            set2.add(i)

        result = set1.intersection(set2)

        assert len(result) == 0

    def test_intersection_empty(self):
        """Test intersection with empty set"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        set1.add(1)
        set1.add(2)

        result = set1.intersection(set2)

        assert len(result) == 0


class TestHashSetDifference:
    """Test difference operation"""

    def test_difference_basic(self):
        """Test basic difference operation"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3, 4]:
            set1.add(i)
        for i in [3, 4, 5, 6]:
            set2.add(i)

        result = set1.difference(set2)

        assert len(result) == 2
        assert 1 in result
        assert 2 in result
        assert 3 not in result
        assert 4 not in result

    def test_difference_disjoint(self):
        """Test difference of disjoint sets"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in range(5):
            set1.add(i)
        for i in range(5, 10):
            set2.add(i)

        result = set1.difference(set2)

        assert len(result) == 5
        for i in range(5):
            assert i in result

    def test_difference_empty(self):
        """Test difference with empty set"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        set1.add(1)
        set1.add(2)

        result = set1.difference(set2)

        assert len(result) == 2
        assert 1 in result
        assert 2 in result


class TestHashSetSubsetSuperset:
    """Test subset and superset operations"""

    def test_is_subset_true(self):
        """Test is_subset when true"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2]:
            set1.add(i)
        for i in [1, 2, 3, 4]:
            set2.add(i)

        assert set1.is_subset(set2)

    def test_is_subset_false(self):
        """Test is_subset when false"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 5]:
            set1.add(i)
        for i in [1, 2, 3, 4]:
            set2.add(i)

        assert not set1.is_subset(set2)

    def test_is_subset_equal(self):
        """Test is_subset with equal sets"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3]:
            set1.add(i)
            set2.add(i)

        assert set1.is_subset(set2)

    def test_is_superset_true(self):
        """Test is_superset when true"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3, 4]:
            set1.add(i)
        for i in [1, 2]:
            set2.add(i)

        assert set1.is_superset(set2)

    def test_is_superset_false(self):
        """Test is_superset when false"""
        set1 = HashSet[int]()
        set2 = HashSet[int]()

        for i in [1, 2, 3]:
            set1.add(i)
        for i in [1, 2, 5]:
            set2.add(i)

        assert not set1.is_superset(set2)


class TestHashSetWithDifferentTypes:
    """Test HashSet with different data types"""

    def test_string_set(self):
        """Test with string elements"""
        hs = HashSet[str]()

        words = ["hello", "world", "python", "test"]
        for word in words:
            hs.add(word)

        assert len(hs) == 4
        for word in words:
            assert word in hs

    def test_tuple_set(self):
        """Test with tuple elements"""
        hs = HashSet[tuple]()

        tuples = [(1, 2), (3, 4), (5, 6)]
        for t in tuples:
            hs.add(t)

        assert len(hs) == 3
        for t in tuples:
            assert t in hs

    def test_mixed_operations(self):
        """Test complex operations with strings"""
        set1 = HashSet[str]()
        set2 = HashSet[str]()

        for word in ["apple", "banana", "cherry"]:
            set1.add(word)
        for word in ["banana", "cherry", "date"]:
            set2.add(word)

        union = set1.union(set2)

        assert len(union) == 4

        intersection = set1.intersection(set2)
        assert len(intersection) == 2
        assert "banana" in intersection
        assert "cherry" in intersection
