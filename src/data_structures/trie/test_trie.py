import pytest
from trie import Trie, Node


class TestTrieNode:
    """Tests for the TrieNode class."""

    def test_node_initialization(self):
        """Test that a new node is properly initialized."""
        node = Node()

        assert node.children == {}
        assert node.is_end_of_word is False


class TestTrieInsert:
    """Tests for the insert operation."""

    def test_insert_single_word(self):
        """Test inserting a single word."""
        trie = Trie()

        trie.insert("hello")

        assert len(trie) == 1
        assert trie.search("hello") is True

    def test_insert_multiple_words(self):
        """Test inserting multiple words."""
        trie = Trie()

        words = ["apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)
        assert len(trie) == 3
        for word in words:
            assert trie.search(word) is True

    def test_insert_duplicate_word(self):
        """Test that inserting a duplicate doesn't increase size."""
        trie = Trie()

        trie.insert("test")
        trie.insert("test")

        assert len(trie) == 1
        assert trie.search("test") is True

    def test_insert_empty_string(self):
        """Test inserting an empty string."""
        trie = Trie()

        trie.insert("")

        assert len(trie) == 0

    def test_insert_words_with_common_prefix(self):
        """Test inserting words that share a common prefix."""
        trie = Trie()

        trie.insert("app")
        trie.insert("apple")
        trie.insert("application")

        assert len(trie) == 3
        assert trie.search("app") is True
        assert trie.search("apple") is True
        assert trie.search("application") is True

    def test_insert_prefix_after_longer_word(self):
        """Test inserting a prefix after a longer word already exists."""
        trie = Trie()

        trie.insert("testing")
        trie.insert("test")

        assert len(trie) == 2
        assert trie.search("test") is True
        assert trie.search("testing") is True


class TestTrieSearch:
    """Tests for the search operation."""

    def test_search_existing_word(self):
        """Test searching for a word that exists."""
        trie = Trie()

        trie.insert("python")

        assert trie.search("python") is True

    def test_search_nonexistent_word(self):
        """Test searching for a word that doesn't exist."""
        trie = Trie()

        trie.insert("python")

        assert trie.search("java") is False

    def test_search_prefix_of_word(self):
        """Test that searching for a prefix returns False."""
        trie = Trie()

        trie.insert("testing")

        assert trie.search("test") is False

    def test_search_empty_string(self):
        """Test searching for an empty string."""
        trie = Trie()

        trie.insert("word")

        assert trie.search("") is False

    def test_search_in_empty_trie(self):
        """Test searching in an empty Trie."""
        trie = Trie()

        assert trie.search("anything") is False

    def test_search_case_sensitive(self):
        """Test that search is case-sensitive."""
        trie = Trie()

        trie.insert("Hello")

        assert trie.search("Hello") is True
        assert trie.search("hello") is False
