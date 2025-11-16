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
