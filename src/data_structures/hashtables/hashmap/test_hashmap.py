import pytest
from typing import Tuple
from hashmap import HashMap


class TestHashMapBasicOperations:
    """Test basic CRUD operations."""

    def test_initialization(self):
        """Test hash map initializes with correct defaults."""
        hm = HashMap()

        assert len(hm) == 0
        assert hm.capacity == 16
        assert hm.size == 0

    def test_initialization_custom_capacity(self):
        """Test hash map initializes with custom capacity."""
        hm = HashMap(initial_capacity=32)

        assert hm.capacity == 32
        assert len(hm) == 0

    def test_put_single_item(self):
        """Test inserting a single key-value pair."""
        hm = HashMap()

        hm.put("key1", "value1")

        assert len(hm) == 1
        assert hm.get("key1") == "value1"

    def test_put_multiple_items(self):
        """Test inserting multiple key-value pairs."""
        hm = HashMap()

        hm.put("apple", 5)
        hm.put("banana", 3)
        hm.put("cherry", 7)

        assert len(hm) == 3
        assert hm.get("apple") == 5
        assert hm.get("banana") == 3
        assert hm.get("cherry") == 7

    def test_put_updates_existing_key(self):
        """Test that put updates value for existing key."""
        hm = HashMap()

        hm.put("key", "old_value")
        hm.put("key", "new_value")

        assert len(hm) == 1
        assert hm.get("key") == "new_value"

    def test_get_existing_key(self):
        """Test retrieving existing key."""
        hm = HashMap()

        hm.put("test", 42)

        assert hm.get("test") == 42

    def test_get_nonexistent_key_raises_keyerror(self):
        """Test that getting nonexistent key raises KeyError."""
        hm = HashMap()

        with pytest.raises(KeyError, match="Key 'missing' not found"):
            hm.get("missing")

    def test_remove_existing_key(self):
        """Test removing an existing key."""
        hm = HashMap()

        hm.put("key", "value")
        removed_value = hm.remove("key")

        assert removed_value == "value"
        assert len(hm) == 0
        with pytest.raises(KeyError):
            hm.get("key")

    def test_remove_nonexistent_key_raises_keyerror(self):
        """Test that removing nonexistent key raises KeyError."""
        hm = HashMap()

        with pytest.raises(KeyError, match="Key 'missing' not found"):
            hm.remove("missing")

    def test_contains_existing_key(self):
        """Test contains returns True for existing key."""
        hm = HashMap()

        hm.put("exists", 1)

        assert hm.contains("exists") is True

    def test_contains_nonexistent_key(self):
        """Test contains returns False for nonexistent key."""
        hm = HashMap()

        assert hm.contains("missing") is False


class TestHashMapCollections:
    """Test methods that return collections of keys/values."""

    def test_keys_empty_map(self):
        """Test keys() on empty map."""
        hm = HashMap()

        assert hm.keys() == []

    def test_keys_returns_all_keys(self):
        """Test keys() returns all keys."""
        hm = HashMap()

        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        keys = hm.keys()

        assert len(keys) == 3
        assert set(keys) == {"a", "b", "c"}

    def test_values_empty_map(self):
        """Test values() on empty map."""
        hm = HashMap()

        assert hm.values() == []

    def test_values_returns_all_values(self):
        """Test values() returns all values."""
        hm = HashMap()

        hm.put("a", 10)
        hm.put("b", 20)
        hm.put("c", 30)

        values = hm.values()

        assert len(values) == 3
        assert set(values) == {10, 20, 30}

    def test_items_empty_map(self):
        """Test items() on empty map."""
        hm = HashMap()

        assert hm.items() == []

    def test_items_returns_all_pairs(self):
        """Test items() returns all key-value pairs."""
        hm = HashMap()

        hm.put("x", 100)
        hm.put("y", 200)

        items = hm.items()

        assert len(items) == 2
        assert set(items) == {("x", 100), ("y", 200)}


class TestHashMapResizing:
    """Test automatic resizing behavior."""

    def test_resize_increases_capacity(self):
        """Test that capacity doubles when load factor exceeded."""
        hm = HashMap(initial_capacity=4)

        initial_capacity = hm.capacity

        # Add items to trigger resize (4 * 0.75 = 3 items)
        for i in range(10):
            hm.put(f"key{i}", i)

        assert hm.capacity > initial_capacity
        assert hm.capacity == 16  # Should double from 4 to 8 to 16

    def test_data_preserved_after_resize(self):
        """Test that all data is preserved after resizing."""
        hm = HashMap(initial_capacity=4)

        # Add many items to force multiple resizes
        test_data = {f"key{i}": i * 10 for i in range(20)}
        for key, value in test_data.items():
            hm.put(key, value)

        # Verify all data is still accessible
        assert len(hm) == 20
        for key, value in test_data.items():
            assert hm.get(key) == value

    def test_resize_maintains_updates(self):
        """Test that updates work correctly across resizes."""
        hm = HashMap(initial_capacity=2)

        # Add initial data
        hm.put("key1", "value1")

        # Force resize by adding more items
        for i in range(10):
            hm.put(f"k{i}", f"v{i}")

        # Update the original key
        hm.put("key1", "updated_value")

        assert hm.get("key1") == "updated_value"
        assert len(hm) == 11  # Not 12, because key1 was updated


class TestHashMapStringRepresentations:
    """Test string and repr methods."""

    def test_str_empty_map(self):
        """Test string representation of empty map."""
        hm = HashMap()

        assert str(hm) == "{}"

    def test_str_with_items(self):
        """Test string representation with items."""
        hm = HashMap()

        hm.put("a", 1)
        result = str(hm)

        assert "'a': 1" in result

    def test_repr_contains_metadata(self):
        """Test repr includes size and capacity."""
        hm = HashMap()

        hm.put("test", 123)
        result = repr(hm)

        assert "HashMap" in result
        assert "size=1" in result
        assert "capacity=" in result

    def test_repr_shows_contents(self):
        """Test repr shows actual contents."""
        hm = HashMap()

        hm.put("key", "value")
        result = repr(hm)

        assert "'key'" in result
        assert "'value'" in result
