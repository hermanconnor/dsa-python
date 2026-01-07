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


class TestTrieStartsWith:
    """Tests for the starts_with operation."""

    def test_starts_with_valid_prefix(self):
        """Test checking a valid prefix."""
        trie = Trie()

        trie.insert("apple")

        assert trie.starts_with("app") is True

    def test_starts_with_invalid_prefix(self):
        """Test checking an invalid prefix."""
        trie = Trie()

        trie.insert("apple")

        assert trie.starts_with("ban") is False

    def test_starts_with_complete_word(self):
        """Test that a complete word is also a valid prefix."""
        trie = Trie()

        trie.insert("test")

        assert trie.starts_with("test") is True

    def test_starts_with_empty_string(self):
        """Test that empty string is a valid prefix."""
        trie = Trie()

        trie.insert("word")

        assert trie.starts_with("") is True

    def test_starts_with_longer_than_word(self):
        """Test prefix longer than any word in Trie."""
        trie = Trie()

        trie.insert("hi")

        assert trie.starts_with("hello") is False


class TestTrieGetAllWordsWithPrefix:
    """Tests for the get_all_words_with_prefix operation."""

    def test_get_words_with_valid_prefix(self):
        """Test getting all words with a valid prefix."""
        trie = Trie()

        words = ["app", "apple", "application", "apply"]
        for word in words:
            trie.insert(word)

        result = trie.get_all_words_with_prefix("app")

        assert set(result) == set(words)

    def test_get_words_with_no_matches(self):
        """Test getting words with a prefix that has no matches."""
        trie = Trie()

        trie.insert("apple")
        result = trie.get_all_words_with_prefix("ban")

        assert result == []

    def test_get_words_with_empty_prefix(self):
        """Test getting all words with empty prefix."""
        trie = Trie()

        words = ["apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)

        result = trie.get_all_words_with_prefix("")

        assert set(result) == set(words)

    def test_get_words_single_match(self):
        """Test getting words when only one word matches."""
        trie = Trie()

        trie.insert("unique")
        trie.insert("test")
        result = trie.get_all_words_with_prefix("uni")

        assert result == ["unique"]

    def test_get_words_from_empty_trie(self):
        """Test getting words from an empty Trie."""
        trie = Trie()

        result = trie.get_all_words_with_prefix("any")

        assert result == []


class TestTrieDisplay:
    """Tests for the display operation."""

    def test_display_sorted_words(self):
        """Test that display returns sorted words."""
        trie = Trie()

        words = ["zebra", "apple", "banana", "cherry"]
        for word in words:
            trie.insert(word)

        result = trie.display()

        assert result == sorted(words)

    def test_display_single_word(self):
        """Test displaying a Trie with one word."""
        trie = Trie()

        trie.insert("single")

        assert trie.display() == ["single"]


class TestTrieLen:
    """Tests for the __len__ method."""

    def test_len_empty_trie(self):
        """Test length of empty Trie."""
        trie = Trie()

        assert len(trie) == 0

    def test_len_after_insertions(self):
        """Test length after multiple insertions."""
        trie = Trie()

        for i in range(5):
            trie.insert(f"word{i}")

        assert len(trie) == 5


class TestTrieContains:
    """Tests for the __contains__ method (in operator)."""

    def test_contains_existing_word(self):
        """Test 'in' operator with existing word."""
        trie = Trie()

        trie.insert("test")

        assert "test" in trie

    def test_contains_nonexistent_word(self):
        """Test 'in' operator with nonexistent word."""
        trie = Trie()

        trie.insert("test")

        assert "other" not in trie


class TestTrieRepr:
    """Tests for the __repr__ method."""

    def test_repr_format(self):
        """Test that repr returns expected format."""
        trie = Trie()

        trie.insert("test")
        repr_str = repr(trie)

        assert "Trie" in repr_str
        assert "size=1" in repr_str

    def test_repr_truncates_long_list(self):
        """Test that repr truncates when many words exist."""
        trie = Trie()

        for i in range(10):
            trie.insert(f"word{i}")
        repr_str = repr(trie)

        assert "..." in repr_str
