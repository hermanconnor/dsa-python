import pytest
from undirected_graph import UndirectedGraph


class TestGraphInitialization:
    """Test graph creation and basic properties."""

    def test_empty_graph_creation(self):
        graph = UndirectedGraph()

        assert graph.is_empty()
        assert len(graph.get_vertices()) == 0
        assert len(graph.get_edges()) == 0

    def test_repr(self):
        graph = UndirectedGraph()

        assert repr(graph) == "UndirectedGraph(vertices=0, edges=0)"

        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_edge(1, 2)

        assert repr(graph) == "UndirectedGraph(vertices=2, edges=1)"

    def test_str_empty_graph(self):
        graph = UndirectedGraph()

        assert str(graph) == "Empty Graph"

    def test_str_with_vertices(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 3, 10)
        output = str(graph)

        assert "1 --" in output
        assert "2(5)" in output or "3(10)" in output
