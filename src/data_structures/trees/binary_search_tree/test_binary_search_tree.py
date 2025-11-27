import pytest
from binary_search_tree import BinarySearchTree, TreeNode


class TestTreeNode:
    """Tests for TreeNode class."""

    def test_node_creation(self):
        node = TreeNode(5)

        assert node.value == 5
        assert node.left is None
        assert node.right is None

    def test_node_repr(self):
        node = TreeNode(10)

        assert repr(node) == "TreeNode(10)"


class TestBinarySearchTreeBasics:
    """Tests for basic BST operations."""

    def test_empty_tree_creation(self):
        tree = BinarySearchTree[int]()

        assert tree.root is None
        assert len(tree) == 0

    def test_single_insert(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree.root is not None
        assert tree.root.value == 5
        assert len(tree) == 1

    def test_multiple_inserts(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)
        tree.insert(3)
        tree.insert(7)

        assert tree.root.value == 5
        assert tree.root.left.value == 3
        assert tree.root.right.value == 7
        assert len(tree) == 3

    def test_duplicate_insert_ignored(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)
        tree.insert(5)

        assert len(tree) == 1


class TestBSTMagicMethods:
    """Tests for magic methods."""

    def test_len_empty_tree(self):
        tree = BinarySearchTree[int]()

        assert len(tree) == 0

    def test_len_non_empty_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 9])

        assert len(tree) == 5

    def test_repr_representation(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])
        repr_str = repr(tree)

        assert "BinarySearchTree" in repr_str
        assert "size=3" in repr_str
