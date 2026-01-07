class Node:
    """A node in the Trie data structure."""

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) data structure implementation.

    A Trie is a tree-like data structure that stores strings efficiently,
    allowing for fast prefix-based operations like autocomplete.
    """

    def __init__(self):
        self.root = Node()
        self._size = 0

    def insert(self, word):
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

    def search(self, word):
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

    def __len__(self):
        """
        Return the number of words in the Trie.

        Returns:
            int: Number of words stored
        """
        return self._size
