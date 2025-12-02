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
