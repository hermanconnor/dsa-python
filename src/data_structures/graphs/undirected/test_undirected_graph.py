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


class TestVertexOperations:
    """Test adding, removing, and checking vertices."""

    def test_add_single_vertex(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)

        assert 1 in graph
        assert not graph.is_empty()
        assert len(graph.get_vertices()) == 1

    def test_add_multiple_vertices(self):
        graph = UndirectedGraph()

        vertices = [1, 2, 3, 'A', 'B']
        for v in vertices:
            graph.add_vertex(v)

        assert len(graph.get_vertices()) == 5
        for v in vertices:
            assert v in graph

    def test_add_duplicate_vertex(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)
        graph.add_vertex(1)  # Adding again

        assert len(graph.get_vertices()) == 1

    def test_remove_vertex(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)

        assert graph.remove_vertex(1)
        assert 1 not in graph
        assert graph.is_empty()

    def test_remove_nonexistent_vertex(self):
        graph = UndirectedGraph()

        assert not graph.remove_vertex(1)

    def test_remove_vertex_with_edges(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        assert graph.remove_vertex(1)
        assert 1 not in graph
        assert 2 in graph
        assert 3 in graph
        # Edge between 2 and 3 should still exist
        assert graph.has_edge(2, 3)
        # Edges with vertex 1 should be gone
        assert not graph.has_edge(2, 1)
        assert not graph.has_edge(3, 1)

    def test_contains_operator(self):
        graph = UndirectedGraph()

        graph.add_vertex('A')

        assert 'A' in graph
        assert 'B' not in graph


class TestEdgeOperations:
    """Test adding, removing, and checking edges."""

    def test_add_edge_creates_vertices(self):
        graph = UndirectedGraph()

        assert graph.add_edge(1, 2)
        assert 1 in graph
        assert 2 in graph

    def test_add_edge_bidirectional(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 10)

        assert graph.has_edge(1, 2)
        assert graph.has_edge(2, 1)
        assert graph.get_edge_weight(1, 2) == 10
        assert graph.get_edge_weight(2, 1) == 10

    def test_add_duplicate_edge(self):
        graph = UndirectedGraph()

        assert graph.add_edge(1, 2)
        assert not graph.add_edge(1, 2)  # Should return False
        assert not graph.add_edge(2, 1)  # Reverse should also fail

    def test_add_self_loop(self):
        graph = UndirectedGraph()

        assert not graph.add_edge(1, 1)  # Self-loop should be prevented

    def test_add_edge_with_weight(self):
        graph = UndirectedGraph()

        graph.add_edge('A', 'B', 5.5)
        assert graph.get_edge_weight('A', 'B') == 5.5

    def test_add_edge_default_weight(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        assert graph.get_edge_weight(1, 2) == 1

    def test_remove_edge(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        assert graph.remove_edge(1, 2)
        assert not graph.has_edge(1, 2)
        assert not graph.has_edge(2, 1)
        # Vertices should still exist
        assert 1 in graph
        assert 2 in graph

    def test_remove_edge_reverse_direction(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        assert graph.remove_edge(2, 1)  # Remove in opposite direction
        assert not graph.has_edge(1, 2)

    def test_remove_nonexistent_edge(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)
        graph.add_vertex(2)

        assert not graph.remove_edge(1, 2)

    def test_has_edge(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)

        assert graph.has_edge(1, 2)
        assert graph.has_edge(2, 1)
        assert not graph.has_edge(1, 3)

    def test_has_edge_nonexistent_vertex(self):
        graph = UndirectedGraph()

        assert not graph.has_edge(1, 2)

    def test_get_edge_weight(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 7)

        assert graph.get_edge_weight(1, 2) == 7
        assert graph.get_edge_weight(2, 1) == 7

    def test_get_edge_weight_nonexistent(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)

        assert graph.get_edge_weight(1, 2) is None

    def test_update_edge_weight(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 5)

        assert graph.update_edge_weight(1, 2, 10)
        assert graph.get_edge_weight(1, 2) == 10
        assert graph.get_edge_weight(2, 1) == 10

    def test_update_nonexistent_edge_weight(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)
        graph.add_vertex(2)

        assert not graph.update_edge_weight(1, 2, 10)

    def test_get_edges(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 10)
        graph.add_edge(1, 3, 15)

        edges = graph.get_edges()

        assert len(edges) == 3

        # Check that each edge appears only once
        edge_set = set()
        for v1, v2, w in edges:
            edge = frozenset([v1, v2])
            assert edge not in edge_set
            edge_set.add(edge)
