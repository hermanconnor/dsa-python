import pytest
from union_find import UnionFind


class TestUnionFindInitialization:
    """Test UnionFind initialization."""

    def test_init_valid_size(self):
        """Test initialization with valid size."""
        uf = UnionFind(5)

        assert len(uf.parent) == 5
        assert len(uf.rank) == 5
        assert uf.components == 5
        assert uf.parent == [0, 1, 2, 3, 4]
        assert uf.rank == [0, 0, 0, 0, 0]

    def test_init_zero_size(self):
        """Test initialization with zero elements."""
        uf = UnionFind(0)

        assert len(uf.parent) == 0
        assert uf.components == 0

    def test_init_negative_size(self):
        """Test initialization with negative size raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            UnionFind(-1)

    def test_init_large_size(self):
        """Test initialization with large size."""
        uf = UnionFind(1000)

        assert len(uf.parent) == 1000
        assert uf.components == 1000


class TestFind:
    """Test find operation."""

    def test_find_initial_state(self):
        """Test find returns element itself initially."""
        uf = UnionFind(5)

        for i in range(5):
            assert uf.find(i) == i

    def test_find_after_union(self):
        """Test find returns correct root after union."""
        uf = UnionFind(5)

        uf.union(0, 1)
        uf.union(1, 2)

        root = uf.find(0)
        assert uf.find(1) == root
        assert uf.find(2) == root

    def test_find_path_compression(self):
        """Test that path compression works."""
        uf = UnionFind(5)
        # Create a chain: 0 -> 1 -> 2 -> 3
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        # Find should compress the path
        root = uf.find(0)
        # After path compression, 0 should point directly to root
        assert uf.parent[0] == root

    def test_find_out_of_bounds_negative(self):
        """Test find raises IndexError for negative index."""
        uf = UnionFind(5)

        with pytest.raises(IndexError, match="Index -1 is out of bounds"):
            uf.find(-1)

    def test_find_out_of_bounds_too_large(self):
        """Test find raises IndexError for index >= n."""
        uf = UnionFind(5)

        with pytest.raises(IndexError, match="Index 5 is out of bounds"):
            uf.find(5)

    def test_find_empty_unionfind(self):
        """Test find on empty UnionFind."""
        uf = UnionFind(0)

        with pytest.raises(IndexError):
            uf.find(0)


class TestUnion:
    """Test union operation."""

    def test_union_two_elements(self):
        """Test basic union of two elements."""
        uf = UnionFind(5)
        result = uf.union(0, 1)

        assert result is True
        assert uf.find(0) == uf.find(1)
        assert uf.components == 4

    def test_union_already_connected(self):
        """Test union returns False when elements already connected."""
        uf = UnionFind(5)

        uf.union(0, 1)
        result = uf.union(0, 1)

        assert result is False
        assert uf.components == 4  # Components shouldn't decrease

    def test_union_chain(self):
        """Test multiple unions creating a chain."""
        uf = UnionFind(5)

        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        assert uf.components == 2
        root = uf.find(0)
        assert uf.find(1) == root
        assert uf.find(2) == root
        assert uf.find(3) == root
        assert uf.find(4) != root

    def test_union_by_rank(self):
        """Test that union by rank optimization works."""
        uf = UnionFind(7)
        # Create two trees of different ranks
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(0, 2)  # Should merge by rank

        # Create another tree
        uf.union(4, 5)
        uf.union(5, 6)

        # The tree with more elements should have higher or equal rank
        assert uf.components == 2

    def test_union_all_elements(self):
        """Test unioning all elements into one component."""
        uf = UnionFind(10)

        for i in range(9):
            uf.union(i, i + 1)

        assert uf.components == 1
        root = uf.find(0)
        for i in range(10):
            assert uf.find(i) == root

    def test_union_invalid_indices(self):
        """Test union with invalid indices raises IndexError."""
        uf = UnionFind(5)

        with pytest.raises(IndexError):
            uf.union(-1, 0)
        with pytest.raises(IndexError):
            uf.union(0, 10)
