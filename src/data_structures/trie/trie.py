from typing import Dict, List, Optional


class Node:
    """A node in the Trie data structure."""

    def __init__(self) -> None:
        self.children: Dict[str, 'Node'] = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    Trie (Prefix Tree) data structure implementation.

    A Trie is a tree-like data structure that stores strings efficiently,
    allowing for fast prefix-based operations like autocomplete.

    Note: This implementation is case-sensitive. Convert inputs to lowercase
    if case-insensitive behavior is desired.
    """

    def __init__(self) -> None:
        """Initialize the Trie with an empty root node."""
        self.root: Node = Node()
        self._size: int = 0

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) in worst case (new path)

        Args:
            word (str): The word to insert
        """
        if not word:
            return

        current = self.root

        for char in word:
            # If character doesn't exist, create new node
            if char not in current.children:
                current.children[char] = Node()

            # Move to the child node
            current = current.children[char]

        # Mark the end of the word (only increment size if new word)
        if not current.is_end_of_word:
            current.is_end_of_word = True
            self._size += 1

    def search(self, word: str) -> bool:
        """
        Search for a complete word in the Trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1)

        Args:
            word (str): The word to search for

        Returns:
            bool: True if word exists, False otherwise
        """
        if not word:
            return False

        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        # Return True only if we reached end of word
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.

        Time Complexity: O(p) where p is the length of the prefix
        Space Complexity: O(1)

        Args:
            prefix (str): The prefix to search for

        Returns:
            bool: True if any word starts with prefix, False otherwise
        """
        if not prefix:
            return True  # Empty prefix matches everything

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

    def get_all_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words in the Trie that start with the given prefix.

        Time Complexity: O(p + n) where p is prefix length, n is number of nodes in subtree
        Space Complexity: O(n + m) where n is number of results, m is max word length
                         (optimized using list + backtracking instead of string concatenation)

        Args:
            prefix (str): The prefix to search for

        Returns:
            list: List of all words with the given prefix
        """
        # First, navigate to the prefix node
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # Prefix doesn't exist
            current = current.children[char]

        # Now collect all words starting from this node
        words: List[str] = []

        def _collect_words(node: Node, path_list: List[str]) -> None:
            if node.is_end_of_word:
                words.append("".join(path_list))

            for char, child_node in node.children.items():
                path_list.append(char)
                _collect_words(child_node, path_list)
                path_list.pop()  # Backtrack

        _collect_words(current, list(prefix))

        return words

    def display(self) -> List[str]:
        """
        Display all words in the Trie (for debugging purposes).

        Returns:
            list: Sorted list of all words in the Trie
        """
        all_words: List[str] = self.get_all_words_with_prefix("")

        return sorted(all_words)

    def __len__(self) -> int:
        """
        Return the number of words in the Trie.

        Returns:
            int: Number of words stored
        """
        return self._size

    def __contains__(self, word: str) -> bool:
        """
        Check if a word exists in the Trie using 'in' operator.

        Args:
            word (str): The word to check

        Returns:
            bool: True if word exists, False otherwise
        """
        return self.search(word)

    def __repr__(self) -> str:
        """String representation of the Trie."""
        return f"Trie(size={self._size}, words={self.display()[:5]}{'...' if self._size > 5 else ''})"
