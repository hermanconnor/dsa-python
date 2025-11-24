import pytest
from directed_matrix_graph import DirectedMatrixGraph


class TestInitialization:
    """Tests for graph initialization."""

    def test_valid_initialization(self):
        """Test creating a graph with valid number of vertices."""
        g = DirectedMatrixGraph(5)

        assert g.num_vertices == 5
        assert len(g.matrix) == 5
        assert all(len(row) == 5 for row in g.matrix)
        assert all(val is None for row in g.matrix for val in row)

    def test_single_vertex_graph(self):
        """Test creating a graph with one vertex."""
        g = DirectedMatrixGraph(1)

        assert g.num_vertices == 1
        assert g.matrix == [[None]]

    def test_invalid_initialization_zero(self):
        """Test that zero vertices raises ValueError."""
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            DirectedMatrixGraph(0)

    def test_invalid_initialization_negative(self):
        """Test that negative vertices raises ValueError."""
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            DirectedMatrixGraph(-5)


class TestAddEdge:
    """Tests for adding edges."""

    def test_add_simple_edge(self):
        """Test adding a basic edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.matrix[0][1] == 5

    def test_add_edge_default_weight(self):
        """Test adding edge with default weight."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1)

        assert g.matrix[0][1] == 1

    def test_add_zero_weight_edge(self):
        """Test that zero-weight edges are properly represented."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 0)

        assert g.matrix[0][1] == 0
        assert g.has_edge(0, 1) is True

    def test_add_negative_weight_edge(self):
        """Test adding edge with negative weight."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, -10)

        assert g.matrix[0][1] == -10

    def test_add_self_loop(self):
        """Test adding a self-loop."""
        g = DirectedMatrixGraph(3)

        g.add_edge(1, 1, 3)

        assert g.matrix[1][1] == 3

    def test_add_edge_overwrites_existing(self):
        """Test that adding an edge overwrites existing weight."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 1, 10)

        assert g.matrix[0][1] == 10

    def test_directed_edge_not_symmetric(self):
        """Test that edges are directional (not symmetric)."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.matrix[0][1] == 5
        assert g.matrix[1][0] is None

    def test_method_chaining(self):
        """Test that multiple edges can be added via chaining."""
        g = DirectedMatrixGraph(4)

        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 7)

        assert g.matrix[0][1] == 5
        assert g.matrix[1][2] == 3
        assert g.matrix[2][3] == 7

    def test_add_edge_invalid_source(self):
        """Test that invalid source vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.add_edge(5, 1, 5)

    def test_add_edge_invalid_destination(self):
        """Test that invalid destination vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.add_edge(0, 10, 5)

    def test_add_edge_negative_index(self):
        """Test that negative vertex index raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.add_edge(-1, 1, 5)


class TestRemoveEdge:
    """Tests for removing edges."""

    def test_remove_existing_edge(self):
        """Test removing an edge that exists."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        result = g.remove_edge(0, 1)

        assert result is True
        assert g.matrix[0][1] is None

    def test_remove_nonexistent_edge(self):
        """Test removing an edge that doesn't exist."""
        g = DirectedMatrixGraph(3)

        result = g.remove_edge(0, 1)

        assert result is False
        assert g.matrix[0][1] is None

    def test_remove_edge_is_directional(self):
        """Test that removing an edge only affects one direction."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        g.add_edge(1, 0, 3)
        g.remove_edge(0, 1)

        assert g.matrix[0][1] is None
        assert g.matrix[1][0] == 3

    def test_remove_edge_invalid_vertex(self):
        """Test that invalid vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.remove_edge(0, 5)


class TestHasEdge:
    """Tests for checking edge existence."""

    def test_has_edge_exists(self):
        """Test has_edge returns True for existing edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.has_edge(0, 1) is True

    def test_has_edge_not_exists(self):
        """Test has_edge returns False for non-existing edge."""
        g = DirectedMatrixGraph(3)

        assert g.has_edge(0, 1) is False

    def test_has_edge_zero_weight(self):
        """Test has_edge returns True for zero-weight edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 0)

        assert g.has_edge(0, 1) is True

    def test_has_edge_directional(self):
        """Test has_edge respects direction."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.has_edge(0, 1) is True
        assert g.has_edge(1, 0) is False

    def test_has_edge_invalid_vertex(self):
        """Test that invalid vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.has_edge(0, 5)


class TestGetWeight:
    """Tests for retrieving edge weights."""

    def test_get_weight_existing_edge(self):
        """Test getting weight of existing edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 15)

        assert g.get_weight(0, 1) == 15

    def test_get_weight_nonexistent_edge(self):
        """Test getting weight of non-existing edge returns None."""
        g = DirectedMatrixGraph(3)

        assert g.get_weight(0, 1) is None

    def test_get_weight_zero(self):
        """Test getting zero weight."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 0)

        assert g.get_weight(0, 1) == 0

    def test_get_weight_negative(self):
        """Test getting negative weight."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, -5)

        assert g.get_weight(0, 1) == -5

    def test_get_weight_invalid_vertex(self):
        """Test that invalid vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.get_weight(0, 5)


class TestGetNeighbors:
    """Tests for retrieving neighbors."""

    def test_get_neighbors_no_edges(self):
        """Test getting neighbors when vertex has no outgoing edges."""
        g = DirectedMatrixGraph(3)

        assert g.get_neighbors(0) == []

    def test_get_neighbors_single_edge(self):
        """Test getting neighbors with one outgoing edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        neighbors = g.get_neighbors(0)

        assert neighbors == [(1, 5)]

    def test_get_neighbors_multiple_edges(self):
        """Test getting neighbors with multiple outgoing edges."""
        g = DirectedMatrixGraph(4)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 3)
        g.add_edge(0, 3, 7)
        neighbors = g.get_neighbors(0)

        assert set(neighbors) == {(1, 5), (2, 3), (3, 7)}

    def test_get_neighbors_includes_self_loop(self):
        """Test that self-loops are included in neighbors."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 0, 2)
        g.add_edge(0, 1, 5)
        neighbors = g.get_neighbors(0)

        assert (0, 2) in neighbors
        assert (1, 5) in neighbors

    def test_get_neighbors_invalid_vertex(self):
        """Test that invalid vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.get_neighbors(5)


class TestDegree:
    """Tests for in-degree and out-degree."""

    def test_out_degree_zero(self):
        """Test out-degree of vertex with no outgoing edges."""
        g = DirectedMatrixGraph(3)

        assert g.get_out_degree(0) == 0

    def test_out_degree_single(self):
        """Test out-degree of vertex with one outgoing edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.get_out_degree(0) == 1

    def test_out_degree_multiple(self):
        """Test out-degree of vertex with multiple outgoing edges."""
        g = DirectedMatrixGraph(4)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 3)
        g.add_edge(0, 3, 7)

        assert g.get_out_degree(0) == 3

    def test_in_degree_zero(self):
        """Test in-degree of vertex with no incoming edges."""
        g = DirectedMatrixGraph(3)

        assert g.get_in_degree(0) == 0

    def test_in_degree_single(self):
        """Test in-degree of vertex with one incoming edge."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)

        assert g.get_in_degree(1) == 1

    def test_in_degree_multiple(self):
        """Test in-degree of vertex with multiple incoming edges."""
        g = DirectedMatrixGraph(4)

        g.add_edge(0, 2, 5)
        g.add_edge(1, 2, 3)
        g.add_edge(3, 2, 7)

        assert g.get_in_degree(2) == 3

    def test_self_loop_affects_both_degrees(self):
        """Test that self-loop contributes to both in and out degree."""
        g = DirectedMatrixGraph(3)

        g.add_edge(1, 1, 5)

        assert g.get_out_degree(1) == 1
        assert g.get_in_degree(1) == 1

    def test_degree_invalid_vertex(self):
        """Test that invalid vertex raises IndexError."""
        g = DirectedMatrixGraph(3)

        with pytest.raises(IndexError, match="out of bounds"):
            g.get_out_degree(5)

        with pytest.raises(IndexError, match="out of bounds"):
            g.get_in_degree(5)


class TestStringRepresentation:
    """Tests for string representation methods."""

    def test_repr(self):
        """Test __repr__ method."""
        g = DirectedMatrixGraph(5)

        assert repr(g) == "DirectedMatrixGraph(num_vertices=5)"

    def test_str_empty_graph(self):
        """Test __str__ for graph with no edges."""
        g = DirectedMatrixGraph(3)

        s = str(g)

        assert "3 vertices" in s
        assert "0 edges" in s

    def test_str_with_edges(self):
        """Test __str__ for graph with edges."""
        g = DirectedMatrixGraph(3)

        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 3)
        s = str(g)

        assert "2 edges" in s
        assert "0 --(5)--> 1" in s
        assert "1 --(3)--> 2" in s
