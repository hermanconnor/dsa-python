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
