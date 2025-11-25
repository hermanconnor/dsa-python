import pytest
from undirected_matrix_graph import UndirectedMatrixGraph


class TestUndirectedMatrixGraphInit:
    """Tests for graph initialization."""

    def test_valid_initialization(self):
        """Test creating a graph with valid number of vertices."""
        g = UndirectedMatrixGraph(5)

        assert g.num_vertices == 5
        assert len(g.matrix) == 5
        assert all(len(row) == 5 for row in g.matrix)
        assert all(g.matrix[i][j] is None
                   for i in range(5) for j in range(5))

    def test_initialization_with_one_vertex(self):
        """Test edge case of single vertex graph."""
        g = UndirectedMatrixGraph(1)

        assert g.num_vertices == 1

    def test_invalid_initialization_zero(self):
        """Test that zero vertices raises ValueError."""
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            UndirectedMatrixGraph(0)

    def test_invalid_initialization_negative(self):
        """Test that negative vertices raises ValueError."""
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            UndirectedMatrixGraph(-5)


class TestAddEdge:
    """Tests for adding edges."""

    def test_add_simple_edge(self):
        """Test adding a basic edge."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.matrix[0][1] == 5
        assert g.matrix[1][0] == 5  # Check symmetry

    def test_add_edge_default_weight(self):
        """Test adding edge with default weight of 1."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 2)

        assert g.matrix[0][2] == 1
        assert g.matrix[2][0] == 1

    def test_add_edge_zero_weight(self):
        """Test that zero-weight edges are supported."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(1, 2, 0)

        assert g.matrix[1][2] == 0
        assert g.matrix[2][1] == 0
        assert g.has_edge(1, 2)

    def test_add_edge_negative_weight(self):
        """Test that negative-weight edges are supported."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, -10)

        assert g.matrix[0][1] == -10
        assert g.matrix[1][0] == -10

    def test_add_edge_overwrite(self):
        """Test that adding an edge overwrites existing edge."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 1, 10)

        assert g.matrix[0][1] == 10
        assert g.matrix[1][0] == 10

    def test_add_edge_to_self(self):
        """Test adding self-loop."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(1, 1, 3)

        assert g.matrix[1][1] == 3

    def test_add_edge_invalid_vertex_negative(self):
        """Test adding edge with negative vertex index."""
        g = UndirectedMatrixGraph(3)

        with pytest.raises(IndexError):
            g.add_edge(-1, 1, 5)

    def test_add_edge_invalid_vertex_out_of_bounds(self):
        """Test adding edge with out-of-bounds vertex."""
        g = UndirectedMatrixGraph(3)

        with pytest.raises(IndexError):
            g.add_edge(0, 5, 5)


class TestRemoveEdge:
    """Tests for removing edges."""

    def test_remove_existing_edge(self):
        """Test removing an edge that exists."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        result = g.remove_edge(0, 1)

        assert result is True
        assert g.matrix[0][1] is None
        assert g.matrix[1][0] is None  # Check both directions removed

    def test_remove_nonexistent_edge(self):
        """Test removing an edge that doesn't exist."""
        g = UndirectedMatrixGraph(3)

        result = g.remove_edge(0, 1)

        assert result is False

    def test_remove_edge_symmetry(self):
        """Test that removing edge works from either direction."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 2, 7)
        g.remove_edge(2, 0)  # Remove from opposite direction

        assert g.matrix[0][2] is None
        assert g.matrix[2][0] is None

    def test_remove_edge_invalid_vertex(self):
        """Test removing edge with invalid vertex."""
        g = UndirectedMatrixGraph(3)

        with pytest.raises(IndexError):
            g.remove_edge(0, 10)


class TestHasEdge:
    """Tests for checking edge existence."""

    def test_has_edge_exists(self):
        """Test checking for existing edge."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.has_edge(0, 1) is True
        assert g.has_edge(1, 0) is True  # Check symmetry

    def test_has_edge_not_exists(self):
        """Test checking for non-existent edge."""
        g = UndirectedMatrixGraph(3)

        assert g.has_edge(0, 1) is False

    def test_has_edge_after_removal(self):
        """Test that has_edge returns False after removal."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(1, 2, 3)
        g.remove_edge(1, 2)

        assert g.has_edge(1, 2) is False

    def test_has_edge_zero_weight(self):
        """Test that zero-weight edges are detected."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 0)

        assert g.has_edge(0, 1) is True


class TestGetWeight:
    """Tests for retrieving edge weights."""

    def test_get_weight_existing_edge(self):
        """Test getting weight of existing edge."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 1, 42)

        assert g.get_weight(0, 1) == 42
        assert g.get_weight(1, 0) == 42  # Check symmetry

    def test_get_weight_nonexistent_edge(self):
        """Test getting weight of non-existent edge."""
        g = UndirectedMatrixGraph(3)

        assert g.get_weight(0, 1) is None

    def test_get_weight_zero(self):
        """Test getting zero weight."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(1, 2, 0)

        assert g.get_weight(1, 2) == 0

    def test_get_weight_negative(self):
        """Test getting negative weight."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(0, 2, -15)

        assert g.get_weight(0, 2) == -15


class TestGetNeighbors:
    """Tests for retrieving vertex neighbors."""

    def test_get_neighbors_single(self):
        """Test getting neighbors when vertex has one neighbor."""
        g = UndirectedMatrixGraph(4)

        g.add_edge(0, 1, 5)
        neighbors = g.get_neighbors(0)

        assert len(neighbors) == 1
        assert (1, 5) in neighbors

    def test_get_neighbors_multiple(self):
        """Test getting neighbors when vertex has multiple neighbors."""
        g = UndirectedMatrixGraph(4)

        g.add_edge(1, 0, 3)
        g.add_edge(1, 2, 7)
        g.add_edge(1, 3, 2)
        neighbors = g.get_neighbors(1)

        assert len(neighbors) == 3
        assert (0, 3) in neighbors
        assert (2, 7) in neighbors
        assert (3, 2) in neighbors

    def test_get_neighbors_none(self):
        """Test getting neighbors when vertex has no neighbors."""
        g = UndirectedMatrixGraph(3)

        neighbors = g.get_neighbors(1)

        assert len(neighbors) == 0

    def test_get_neighbors_self_loop(self):
        """Test that self-loops appear in neighbors."""
        g = UndirectedMatrixGraph(3)

        g.add_edge(1, 1, 5)
        neighbors = g.get_neighbors(1)

        assert (1, 5) in neighbors
