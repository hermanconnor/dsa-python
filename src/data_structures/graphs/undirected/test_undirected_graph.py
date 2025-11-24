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


class TestNeighborsAndDegree:
    """Test neighbor retrieval and degree calculations."""

    def test_get_neighbors(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 3, 10)
        neighbors = graph.get_neighbors(1)

        assert len(neighbors) == 2

        neighbor_vertices = [v for v, w in neighbors]

        assert 2 in neighbor_vertices
        assert 3 in neighbor_vertices

    def test_get_neighbors_nonexistent_vertex(self):
        graph = UndirectedGraph()

        with pytest.raises(ValueError, match="Vertex 1 not in graph"):
            graph.get_neighbors(1)

    def test_degree(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)

        assert graph.degree(1) == 3
        assert graph.degree(2) == 1
        assert graph.degree(3) == 1
        assert graph.degree(4) == 1

    def test_degree_isolated_vertex(self):
        graph = UndirectedGraph()

        graph.add_vertex(1)

        assert graph.degree(1) == 0

    def test_degree_nonexistent_vertex(self):
        graph = UndirectedGraph()

        with pytest.raises(ValueError, match="Vertex 1 not in graph"):
            graph.degree(1)


class TestUtilityMethods:
    """Test utility methods like copy, clear, etc."""

    def test_copy(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 10)

        copied = graph.copy()

        # Check structure is identical
        assert set(copied.get_vertices()) == set(graph.get_vertices())
        assert copied.has_edge(1, 2)
        assert copied.get_edge_weight(1, 2) == 5

        # Modify original and ensure copy is unaffected
        graph.add_edge(3, 4)
        assert not copied.has_edge(3, 4)
        assert 4 not in copied

    def test_clear(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(2, 3)

        graph.clear()

        assert graph.is_empty()
        assert len(graph.get_vertices()) == 0
        assert len(graph.get_edges()) == 0

    def test_is_empty(self):
        graph = UndirectedGraph()

        assert graph.is_empty()

        graph.add_vertex(1)
        assert not graph.is_empty()

        graph.remove_vertex(1)
        assert graph.is_empty()


class TestTraversal:
    """Test DFS and BFS traversal algorithms."""

    def test_dfs_simple_path(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        result = graph.dfs(1)

        assert len(result) == 4
        assert result[0] == 1
        assert set(result) == {1, 2, 3, 4}

    def test_dfs_disconnected_component(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(3, 4)  # Separate component

        result = graph.dfs(1)

        assert set(result) == {1, 2}
        assert 3 not in result
        assert 4 not in result

    def test_dfs_nonexistent_start(self):
        graph = UndirectedGraph()

        with pytest.raises(ValueError, match="Vertex 1 not in graph"):
            graph.dfs(1)

    def test_bfs_simple_path(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        result = graph.bfs(1)

        assert len(result) == 4
        assert result[0] == 1
        assert set(result) == {1, 2, 3, 4}

    def test_bfs_level_order(self):
        graph = UndirectedGraph()

        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        graph.add_edge(2, 5)

        result = graph.bfs(1)
        assert result[0] == 1
        # Level 1: 2 and 3 should come before level 2
        assert result.index(2) < result.index(4)
        assert result.index(2) < result.index(5)
        assert result.index(3) < result.index(4)
        assert result.index(3) < result.index(5)

    def test_bfs_nonexistent_start(self):
        graph = UndirectedGraph()

        with pytest.raises(ValueError, match="Vertex 1 not in graph"):
            graph.bfs(1)
