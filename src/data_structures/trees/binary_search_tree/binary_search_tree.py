from collections import deque
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

    def search(self, value: T) -> bool:
        """
        Searches for a value in the binary search tree (iterative).

        Time Complexity: O(log n) average, O(n) worst-case (unbalanced tree).
        """
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self):
        pass

    def preorder_traversal(self) -> List[T]:
        """
        Performs a preorder traversal (Root-Left-Right).

        Time Complexity: O(n).
        """
        result: List[T] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[TreeNode[T]], result: List[T]) -> None:
        """Recursively performs preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inorder_traversal(self) -> List[T]:
        """
        Performs an inorder traversal (Left-Root-Right). Returns a sorted list.

        Time Complexity: O(n).
        """
        result: List[T] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode[T]], result: List[T]) -> None:
        """Recursively performs inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def postorder_traversal(self) -> List[T]:
        """
        Performs a postorder traversal (Left-Right-Root).

        Time Complexity: O(n).
        """
        result: List[T] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[TreeNode[T]], result: List[T]) -> None:
        """Recursively performs postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def levelorder_traversal(self) -> List[List[T]]:
        """
        Performs a level-order traversal (Breadth-First Search). Returns a list of levels.

        Time Complexity: O(n).
        """
        if not self.root:
            return []

        result: List[List[T]] = []
        queue: Deque[TreeNode[T]] = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level: List[T] = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

    def height(self) -> int:
        """
        Returns the height of the tree (longest path from root to leaf).

        Time Complexity: O(n).
        """
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Optional[TreeNode[T]]) -> int:
        """Recursively calculates the height of a subtree."""
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def min_value(self) -> T:
        """
        Returns the minimum value in the binary search tree.

        Time Complexity: O(log n) average, O(n) worst-case (unbalanced tree).
        Raises:
            ValueError: If the tree is empty.
        """
        if self.root is None:
            raise ValueError("Tree is empty")

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value

    def max_value(self) -> T:
        """
        Returns the maximum value in the binary search tree.

        Time Complexity: O(log n) average, O(n) worst-case (unbalanced tree).
        Raises:
            ValueError: If the tree is empty.
        """
        if self.root is None:
            raise ValueError("Tree is empty")

        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def is_balanced(self):
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

    def __contains__(self, value: T) -> bool:
        """
        Checks if a value exists in the tree (enables 'in' operator).

        Time Complexity: O(log n) average, O(n) worst-case.
        """
        return self.search(value)

    def __iter__(self) -> Iterator[T]:
        """
        Returns an iterator over tree values (inorder traversal).

        Time Complexity: O(n) for full iteration.
        """
        return iter(self.inorder_traversal())

    def __str__(self) -> str:
        """Returns a string representation of the BST (inorder traversal)."""
        return f"BinarySearchTree(inorder={self.inorder_traversal()})"

    def __repr__(self) -> str:
        """Returns a more detailed string representation for debugging."""
        return f"BinarySearchTree(root={repr(self.root)}, size={len(self)})"
