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
