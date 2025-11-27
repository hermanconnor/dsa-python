from typing import Generic, List, Optional, Deque, TypeVar, Iterator

T = TypeVar('T')


class TreeNode(Generic[T]):
    """Represents a node in a binary search tree."""

    def __init__(self, value) -> None:
        """Initializes a TreeNode with a given value."""
        self.value: T = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None

    def __repr__(self) -> str:
        """Returns a string representation of the TreeNode."""
        return f"TreeNode({repr(self.value)})"


class BinarySearchTree(Generic[T]):
    """Implements a binary search tree data structure."""

    def __init__(self) -> None:
        """Initializes an empty BinarySearchTree."""
        self.root: Optional[TreeNode[T]] = None

    def insert(self, value: T) -> None:
        """
        Inserts a new value into the binary search tree (iterative).

        Time Complexity: O(log n) average, O(n) worst-case (unbalanced tree).
        """
        new_node = TreeNode(value)

        # Case 1: Tree is empty. New node becomes the root.
        if self.root is None:
            self.root = new_node
            return

        # Case 2: Tree is not empty. Find the insertion spot.
        current = self.root
        while True:
            if value < current.value:
                # Value belongs in the left subtree
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                # Value belongs in the right subtree
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:  # Duplicate value - do nothing.
                return

    def insert_many(self, values: List[T]) -> None:
        """
        Inserts multiple values into the tree.

        Time Complexity: O(n * log m) where n is number of values, m is tree size.
        """
        for value in values:
            self.insert(value)

    def search(self):
        pass

    def delete(self):
        pass

    def height(self):
        pass

    def is_balanced(self):
        pass

    def preorder_traversal(self):
        pass

    def inorder_traversal(self):
        pass

    def postorder_traversal(self):
        pass

    def levelorder_traversal(self):
        pass

    def _size_recursive(self, node: Optional[TreeNode[T]]) -> int:
        """Recursively calculates the number of nodes in a subtree."""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def __len__(self) -> int:
        """
        Returns the number of nodes in the BST.

        Time Complexity: O(n).
        """
        return self._size_recursive(self.root)

    def __str__(self):
        pass

    def __repr__(self) -> str:
        """Returns a more detailed string representation for debugging."""
        return f"BinarySearchTree(root={repr(self.root)}, size={len(self)})"
