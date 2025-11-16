import pytest
from directed_graph import DirectedGraph


class TestDirectedGraphInitialization:
    """Test graph initialization."""

    def test_empty_graph_initialization(self):
        """Test that a new graph is empty."""
        g = DirectedGraph()

        assert g.is_empty()
        assert len(g.get_vertices()) == 0
        assert len(g.get_edges()) == 0

    def test_repr(self):
        """Test __repr__ method."""
        g = DirectedGraph()

        assert repr(g) == "DirectedGraph(vertices=0, edges=0)"

        g.add_edge('A', 'B')

        assert repr(g) == "DirectedGraph(vertices=2, edges=1)"


class TestVertexOperations:
    """Test vertex addition and removal."""

    def test_add_single_vertex(self):
        """Test adding a single vertex."""
        g = DirectedGraph()

        g.add_vertex('A')

        assert 'A' in g.get_vertices()
        assert not g.is_empty()

    def test_add_multiple_vertices(self):
        """Test adding multiple vertices."""
        g = DirectedGraph()

        vertices = ['A', 'B', 'C', 'D']
        for v in vertices:
            g.add_vertex(v)

        assert set(g.get_vertices()) == set(vertices)

    def test_add_duplicate_vertex(self):
        """Test that adding duplicate vertex doesn't cause issues."""
        g = DirectedGraph()

        g.add_vertex('A')
        g.add_vertex('A')

        assert g.get_vertices().count('A') == 1

    def test_remove_vertex(self):
        """Test removing a vertex."""
        g = DirectedGraph()

        g.add_vertex('A')
        result = g.remove_vertex('A')

        assert result is True
        assert 'A' not in g.get_vertices()

    def test_remove_nonexistent_vertex(self):
        """Test removing a vertex that doesn't exist."""
        g = DirectedGraph()

        result = g.remove_vertex('Z')

        assert result is False

    def test_remove_vertex_removes_connected_edges(self):
        """Test that removing a vertex removes all connected edges."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'B')
        g.remove_vertex('B')

        assert 'B' not in g.get_vertices()
        assert not g.has_edge('A', 'B')
        assert not g.has_edge('C', 'B')
        # A and C should still exist
        assert 'A' in g.get_vertices()
        assert 'C' in g.get_vertices()


class TestEdgeOperations:
    """Test edge addition, removal, and queries."""

    def test_add_edge(self):
        """Test adding an edge."""
        g = DirectedGraph()

        result = g.add_edge('A', 'B')

        assert result is True
        assert g.has_edge('A', 'B')

    def test_add_edge_creates_vertices(self):
        """Test that adding an edge creates vertices if they don't exist."""
        g = DirectedGraph()

        g.add_edge('A', 'B')

        assert 'A' in g.get_vertices()
        assert 'B' in g.get_vertices()

    def test_add_edge_with_weight(self):
        """Test adding a weighted edge."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 5.5)

        assert g.get_edge_weight('A', 'B') == 5.5

    def test_add_duplicate_edge(self):
        """Test that duplicate edges are prevented."""
        g = DirectedGraph()

        result1 = g.add_edge('A', 'B')
        result2 = g.add_edge('A', 'B')

        assert result1 is True
        assert result2 is False
        # Should only have one edge
        assert len(g.get_edges()) == 1

    def test_directed_edge(self):
        """Test that edges are directed."""
        g = DirectedGraph()

        g.add_edge('A', 'B')

        assert g.has_edge('A', 'B')
        assert not g.has_edge('B', 'A')

    def test_remove_edge(self):
        """Test removing an edge."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        result = g.remove_edge('A', 'B')

        assert result is True
        assert not g.has_edge('A', 'B')

    def test_remove_nonexistent_edge(self):
        """Test removing an edge that doesn't exist."""
        g = DirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        result = g.remove_edge('A', 'B')

        assert result is False

    def test_has_edge(self):
        """Test edge existence checking."""
        g = DirectedGraph()

        g.add_edge('A', 'B')

        assert g.has_edge('A', 'B')
        assert not g.has_edge('B', 'A')
        assert not g.has_edge('A', 'C')

    def test_get_edge_weight(self):
        """Test getting edge weight."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 10)

        assert g.get_edge_weight('A', 'B') == 10
        assert g.get_edge_weight('B', 'A') is None

    def test_get_edges(self):
        """Test getting all edges."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'A', 3)
        edges = g.get_edges()

        assert len(edges) == 3
        assert ('A', 'B', 1) in edges
        assert ('B', 'C', 2) in edges
        assert ('C', 'A', 3) in edges


class TestGraphOperations:
    """Test graph-level operations."""

    def test_clear(self):
        """Test clearing the graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.clear()

        assert g.is_empty()
        assert len(g.get_vertices()) == 0
        assert len(g.get_edges()) == 0

    def test_is_empty(self):
        """Test is_empty method."""
        g = DirectedGraph()

        assert g.is_empty()

        g.add_vertex('A')

        assert not g.is_empty()


class TestStringRepresentation:
    """Test string representations."""

    def test_str_empty_graph(self):
        """Test string representation of empty graph."""
        g = DirectedGraph()

        assert str(g) == "Empty Graph"

    def test_str_with_edges(self):
        """Test string representation with edges."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 1)
        g.add_edge('A', 'C', 2)
        result = str(g)

        assert 'A -> B(1), C(2)' in result

    def test_str_vertex_no_edges(self):
        """Test string representation of vertex with no edges."""
        g = DirectedGraph()

        g.add_vertex('A')
        result = str(g)

        assert 'A -> []' in result
