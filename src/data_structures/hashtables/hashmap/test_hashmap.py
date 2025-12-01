import pytest
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
