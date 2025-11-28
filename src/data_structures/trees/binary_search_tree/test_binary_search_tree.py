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

    def test_bool_empty_tree(self):
        tree = BinarySearchTree[int]()

        assert not tree

    def test_bool_non_empty_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree

    def test_str_representation(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])

        assert str(tree) == "BinarySearchTree(inorder=[3, 5, 7])"

    def test_repr_representation(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])
        repr_str = repr(tree)

        assert "BinarySearchTree" in repr_str
        assert "size=3" in repr_str


class TestBSTHeight:
    """Tests for height calculation."""

    def test_empty_tree_height(self):
        tree = BinarySearchTree[int]()

        assert tree.height() == 0

    def test_single_node_height(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree.height() == 1

    def test_balanced_tree_height(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])

        assert tree.height() == 2

    def test_unbalanced_tree_height(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([1, 2, 3, 4, 5])  # Creates a right-skewed tree

        assert tree.height() == 5


class TestBSTMinMax:
    """Tests for min/max value operations."""

    def test_min_value_empty_tree(self):
        tree = BinarySearchTree[int]()

        with pytest.raises(ValueError, match="Tree is empty"):
            tree.min_value()

    def test_max_value_empty_tree(self):
        tree = BinarySearchTree[int]()

        with pytest.raises(ValueError, match="Tree is empty"):
            tree.max_value()

    def test_min_value(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 9])

        assert tree.min_value() == 1

    def test_max_value(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 9])

        assert tree.max_value() == 9

    def test_min_max_single_node(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree.min_value() == 5
        assert tree.max_value() == 5


class TestBSTSearch:
    """Tests for search operations."""

    def test_search_empty_tree(self):
        tree = BinarySearchTree[int]()

        assert not tree.search(5)

    def test_search_existing_value(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 9])

        assert tree.search(5)
        assert tree.search(3)
        assert tree.search(7)
        assert tree.search(1)
        assert tree.search(9)

    def test_search_non_existing_value(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])

        assert not tree.search(10)
        assert not tree.search(0)
        assert not tree.search(4)

    def test_contains_operator(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])

        assert 5 in tree
        assert 3 in tree
        assert 10 not in tree


class TestBSTTraversals:
    """Tests for tree traversal methods."""

    @pytest.fixture
    def sample_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 4, 6, 9])

        return tree

    def test_inorder_traversal(self, sample_tree):
        assert sample_tree.inorder_traversal() == [1, 3, 4, 5, 6, 7, 9]

    def test_preorder_traversal(self, sample_tree):
        assert sample_tree.preorder_traversal() == [5, 3, 1, 4, 7, 6, 9]

    def test_postorder_traversal(self, sample_tree):
        assert sample_tree.postorder_traversal() == [1, 4, 3, 6, 9, 7, 5]

    def test_levelorder_traversal(self, sample_tree):
        expected = [[5], [3, 7], [1, 4, 6, 9]]

        assert sample_tree.levelorder_traversal() == expected

    def test_empty_tree_traversals(self):
        tree = BinarySearchTree[int]()

        assert tree.inorder_traversal() == []
        assert tree.preorder_traversal() == []
        assert tree.postorder_traversal() == []
        assert tree.levelorder_traversal() == []

    def test_single_node_traversals(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree.inorder_traversal() == [5]
        assert tree.preorder_traversal() == [5]
        assert tree.postorder_traversal() == [5]
        assert tree.levelorder_traversal() == [[5]]


class TestBSTDelete:
    """Tests for delete operations."""

    def test_delete_from_empty_tree(self):
        tree = BinarySearchTree[int]()

        with pytest.raises(ValueError, match="Cannot delete from an empty tree"):
            tree.delete(5)

    def test_delete_non_existing_value(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        with pytest.raises(ValueError, match="Value 10 not found in tree"):
            tree.delete(10)

    def test_delete_leaf_node(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])
        tree.delete(3)

        assert 3 not in tree
        assert len(tree) == 2
        assert tree.inorder_traversal() == [5, 7]

    def test_delete_node_with_one_child(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 6])
        tree.delete(7)

        assert 7 not in tree
        assert 6 in tree
        assert len(tree) == 3
        assert tree.inorder_traversal() == [3, 5, 6]

    def test_delete_node_with_two_children(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 4, 6, 9])
        tree.delete(3)

        assert 3 not in tree
        assert len(tree) == 6
        assert tree.inorder_traversal() == [1, 4, 5, 6, 7, 9]

    def test_delete_root_node(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])
        tree.delete(5)

        assert 5 not in tree
        assert len(tree) == 2
        assert tree.inorder_traversal() == [3, 7]


class TestBSTBalance:
    """Tests for balance checking."""

    def test_empty_tree_balanced(self):
        tree = BinarySearchTree[int]()

        assert tree.is_balanced()

    def test_single_node_balanced(self):
        tree = BinarySearchTree[int]()

        tree.insert(5)

        assert tree.is_balanced()

    def test_balanced_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 4, 6, 9])

        assert tree.is_balanced()

    def test_unbalanced_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([1, 2, 3, 4, 5])  # Right-skewed tree

        assert not tree.is_balanced()

    def test_slightly_unbalanced_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 4, 9])
        tree.delete(9)

        assert tree.is_balanced()  # Still balanced (diff <= 1)


class TestBSTIterator:
    """Tests for iterator protocol."""

    def test_iterate_empty_tree(self):
        tree = BinarySearchTree[int]()

        values = list(tree)

        assert values == []

    def test_iterate_tree(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7, 1, 9])
        values = list(tree)

        assert values == [1, 3, 5, 7, 9]  # Inorder traversal

    def test_for_loop(self):
        tree = BinarySearchTree[int]()

        tree.insert_many([5, 3, 7])

        result = []
        for value in tree:
            result.append(value)

        assert result == [3, 5, 7]
