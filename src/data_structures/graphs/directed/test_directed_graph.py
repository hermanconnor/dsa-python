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

    def test_update_edge_weight(self):
        """Test updating edge weight."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 5)
        result = g.update_edge_weight('A', 'B', 15)

        assert result is True
        assert g.get_edge_weight('A', 'B') == 15

    def test_update_nonexistent_edge_weight(self):
        """Test updating weight of nonexistent edge."""
        g = DirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        result = g.update_edge_weight('A', 'B', 10)

        assert result is False

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


class TestNeighborsAndDegrees:
    """Test neighbor queries and degree calculations."""

    def test_get_neighbors(self):
        """Test getting neighbors of a vertex."""
        g = DirectedGraph()

        g.add_edge('A', 'B', 1)
        g.add_edge('A', 'C', 2)
        neighbors = g.get_neighbors('A')

        assert len(neighbors) == 2
        assert ('B', 1) in neighbors
        assert ('C', 2) in neighbors

    def test_get_neighbors_empty(self):
        """Test getting neighbors of vertex with no outgoing edges."""
        g = DirectedGraph()

        g.add_vertex('A')
        neighbors = g.get_neighbors('A')

        assert neighbors == []

    def test_get_neighbors_nonexistent_vertex(self):
        """Test getting neighbors of nonexistent vertex raises error."""
        g = DirectedGraph()

        with pytest.raises(ValueError, match="Vertex Z not in graph"):
            g.get_neighbors('Z')

    def test_in_degree(self):
        """Test in-degree calculation."""
        g = DirectedGraph()

        g.add_edge('A', 'C')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')

        assert g.in_degree('A') == 0
        assert g.in_degree('B') == 0
        assert g.in_degree('C') == 2
        assert g.in_degree('D') == 1

    def test_out_degree(self):
        """Test out-degree calculation."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'C')

        assert g.out_degree('A') == 2
        assert g.out_degree('B') == 1
        assert g.out_degree('C') == 0

    def test_degree_nonexistent_vertex(self):
        """Test that degree methods raise error for nonexistent vertex."""
        g = DirectedGraph()

        with pytest.raises(ValueError):
            g.in_degree('Z')

        with pytest.raises(ValueError):
            g.out_degree('Z')

    def test_in_degree_after_edge_removal(self):
        """Test that in-degree updates correctly after edge removal."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('C', 'B')

        assert g.in_degree('B') == 2

        g.remove_edge('A', 'B')
        assert g.in_degree('B') == 1


class TestTraversals:
    """Test DFS and BFS traversals."""

    def test_dfs_linear_graph(self):
        """Test DFS on a linear graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        result = g.dfs('A')

        assert result == ['A', 'B', 'C', 'D']

    def test_dfs_branching_graph(self):
        """Test DFS on a branching graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'D')
        result = g.dfs('A')

        assert result[0] == 'A'
        assert 'D' in result
        assert len(result) == 4

    def test_dfs_with_cycle(self):
        """Test DFS on graph with cycle."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        result = g.dfs('A')

        # Should visit each vertex exactly once
        assert len(result) == 3
        assert set(result) == {'A', 'B', 'C'}

    def test_dfs_single_vertex(self):
        """Test DFS on single vertex."""
        g = DirectedGraph()

        g.add_vertex('A')
        result = g.dfs('A')

        assert result == ['A']

    def test_dfs_nonexistent_vertex(self):
        """Test DFS raises error for nonexistent vertex."""
        g = DirectedGraph()

        with pytest.raises(ValueError):
            g.dfs('Z')

    def test_bfs_linear_graph(self):
        """Test BFS on a linear graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        result = g.bfs('A')

        assert result == ['A', 'B', 'C', 'D']

    def test_bfs_level_order(self):
        """Test BFS visits vertices level by level."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'E')
        result = g.bfs('A')

        assert result[0] == 'A'
        # B and C should come before D and E
        b_idx = result.index('B')
        c_idx = result.index('C')
        d_idx = result.index('D')
        e_idx = result.index('E')

        assert b_idx < d_idx
        assert c_idx < e_idx

    def test_bfs_nonexistent_vertex(self):
        """Test BFS raises error for nonexistent vertex."""
        g = DirectedGraph()

        with pytest.raises(ValueError):
            g.bfs('Z')


class TestCycleDetection:
    """Test cycle detection."""

    def test_has_cycle_acyclic(self):
        """Test cycle detection on acyclic graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('A', 'C')

        assert not g.has_cycle()

    def test_has_cycle_with_cycle(self):
        """Test cycle detection on graph with cycle."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')

        assert g.has_cycle()

    def test_has_cycle_self_loop(self):
        """Test cycle detection with self-loop."""
        g = DirectedGraph()

        g.add_edge('A', 'A')
        assert g.has_cycle()

    def test_has_cycle_empty_graph(self):
        """Test cycle detection on empty graph."""
        g = DirectedGraph()
        assert not g.has_cycle()

    def test_has_cycle_disconnected_with_cycle(self):
        """Test cycle detection with disconnected components."""
        g = DirectedGraph()

        # Component 1: no cycle
        g.add_edge('A', 'B')
        # Component 2: has cycle
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'C')

        assert g.has_cycle()


class TestTopologicalSort:
    """Test topological sorting."""

    def test_topological_sort_linear(self):
        """Test topological sort on linear graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        result = g.topological_sort()

        assert result == ['A', 'B', 'C', 'D']

    def test_topological_sort_dag(self):
        """Test topological sort on DAG."""
        g = DirectedGraph()

        g.add_edge('A', 'C')
        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'E')
        g.add_edge('D', 'E')
        result = g.topological_sort()

        # Verify valid topological order
        assert result.index('A') < result.index('C')
        assert result.index('B') < result.index('C')
        assert result.index('B') < result.index('D')
        assert result.index('C') < result.index('E')
        assert result.index('D') < result.index('E')

    def test_topological_sort_with_cycle(self):
        """Test topological sort returns None for graph with cycle."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        result = g.topological_sort()

        assert result is None

    def test_topological_sort_empty_graph(self):
        """Test topological sort on empty graph."""
        g = DirectedGraph()

        result = g.topological_sort()

        assert result == []


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


class TestReverse:
    """Tests for the reverse() method."""

    def test_reverse_empty_graph(self):
        """Test reversing an empty graph."""
        g = DirectedGraph()

        reversed_graph = g.reverse()

        assert reversed_graph.is_empty()
        assert reversed_graph.get_vertices() == []

    def test_reverse_single_vertex(self):
        """Test reversing a graph with a single vertex and no edges."""
        g = DirectedGraph()

        g.add_vertex('A')
        reversed_graph = g.reverse()

        assert 'A' in reversed_graph
        assert reversed_graph.get_neighbors('A') == []

    def test_reverse_simple_edge(self):
        """Test reversing a simple directed edge."""
        g = DirectedGraph()

        g.add_edge('A', 'B', weight=5)
        reversed_graph = g.reverse()

        # Original: A -> B
        # Reversed: B -> A
        assert reversed_graph.has_edge('B', 'A')
        assert not reversed_graph.has_edge('A', 'B')
        assert reversed_graph.get_edge_weight('B', 'A') == 5

    def test_reverse_chain(self):
        """Test reversing a chain of vertices."""
        g = DirectedGraph()
        # Create chain: A -> B -> C -> D
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')

        reversed_graph = g.reverse()

        # Reversed: D -> C -> B -> A
        assert reversed_graph.has_edge('D', 'C')
        assert reversed_graph.has_edge('C', 'B')
        assert reversed_graph.has_edge('B', 'A')
        assert not reversed_graph.has_edge('A', 'B')

    def test_reverse_cycle(self):
        """Test reversing a cycle."""
        g = DirectedGraph()
        # Create cycle: A -> B -> C -> A
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')

        reversed_graph = g.reverse()

        # Reversed cycle: A -> C -> B -> A
        assert reversed_graph.has_edge('B', 'A')
        assert reversed_graph.has_edge('C', 'B')
        assert reversed_graph.has_edge('A', 'C')

    def test_reverse_preserves_weights(self):
        """Test that reversing preserves edge weights."""
        g = DirectedGraph()

        g.add_edge('A', 'B', weight=10)
        g.add_edge('B', 'C', weight=20)
        g.add_edge('A', 'C', weight=30)

        reversed_graph = g.reverse()

        assert reversed_graph.get_edge_weight('B', 'A') == 10
        assert reversed_graph.get_edge_weight('C', 'B') == 20
        assert reversed_graph.get_edge_weight('C', 'A') == 30

    def test_reverse_twice_equals_original(self):
        """Test that reversing twice returns to original structure."""
        g = DirectedGraph()

        g.add_edge('A', 'B', weight=5)
        g.add_edge('B', 'C', weight=10)
        g.add_edge('A', 'C', weight=15)

        double_reversed = g.reverse().reverse()

        # Check all edges are restored
        assert double_reversed.has_edge('A', 'B')
        assert double_reversed.has_edge('B', 'C')
        assert double_reversed.has_edge('A', 'C')
        assert double_reversed.get_edge_weight('A', 'B') == 5
        assert double_reversed.get_edge_weight('B', 'C') == 10
        assert double_reversed.get_edge_weight('A', 'C') == 15


class TestCopy:
    """Tests for the copy() method."""

    def test_copy_empty_graph(self):
        """Test copying an empty graph."""
        g = DirectedGraph()

        copied = g.copy()
        assert copied.is_empty()
        assert copied.get_vertices() == []

    def test_copy_single_vertex(self):
        """Test copying a graph with a single vertex."""
        g = DirectedGraph()

        g.add_vertex('A')
        copied = g.copy()

        assert 'A' in copied
        assert copied.get_neighbors('A') == []

    def test_copy_basic_structure(self):
        """Test that copy preserves basic graph structure."""
        g = DirectedGraph()

        g.add_edge('A', 'B', weight=5)
        g.add_edge('B', 'C', weight=10)
        g.add_edge('A', 'C', weight=15)

        copied = g.copy()

        assert copied.has_edge('A', 'B')
        assert copied.has_edge('B', 'C')
        assert copied.has_edge('A', 'C')
        assert copied.get_edge_weight('A', 'B') == 5
        assert copied.get_edge_weight('B', 'C') == 10
        assert copied.get_edge_weight('A', 'C') == 15

    def test_copy_independence(self):
        """Test that copied graph is independent from original."""
        g = DirectedGraph()

        g.add_edge('A', 'B', weight=5)
        copied = g.copy()

        # Modify original
        g.add_edge('B', 'C', weight=10)
        g.update_edge_weight('A', 'B', 100)

        # Copy should be unchanged
        assert not copied.has_edge('B', 'C')
        assert copied.get_edge_weight('A', 'B') == 5

    def test_copy_vertex_independence(self):
        """Test that adding/removing vertices doesn't affect copy."""
        g = DirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        copied = g.copy()

        # Add vertex to original
        g.add_vertex('C')

        # Remove vertex from copy
        copied.remove_vertex('B')

        # Check independence
        assert 'C' not in copied
        assert 'B' in g

    def test_copy_preserves_in_degrees(self):
        """Test that copy preserves in-degree counts."""
        g = DirectedGraph()

        g.add_edge('A', 'C')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')

        copied = g.copy()

        assert copied.in_degree('C') == 2
        assert copied.in_degree('D') == 1
        assert copied.in_degree('A') == 0

    def test_copy_complex_graph(self):
        """Test copying a more complex graph."""
        g = DirectedGraph()
        # Create a graph with multiple components
        g.add_edge('A', 'B', weight=1)
        g.add_edge('B', 'C', weight=2)
        g.add_edge('C', 'A', weight=3)  # Cycle
        g.add_edge('D', 'E', weight=4)  # Separate component

        copied = g.copy()

        # Verify structure
        assert set(copied.get_vertices()) == {'A', 'B', 'C', 'D', 'E'}
        assert copied.has_cycle()
        assert len(copied.get_edges()) == 4


class TestWeaklyConnectedComponents:
    """Tests for the weakly_connected_components() method."""

    def test_wcc_empty_graph(self):
        """Test WCC on an empty graph."""
        g = DirectedGraph()

        components = g.weakly_connected_components()
        assert components == []

    def test_wcc_single_vertex(self):
        """Test WCC with a single isolated vertex."""
        g = DirectedGraph()

        g.add_vertex('A')
        components = g.weakly_connected_components()

        assert len(components) == 1
        assert 'A' in components[0]

    def test_wcc_fully_connected(self):
        """Test WCC on a fully connected graph."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')

        components = g.weakly_connected_components()

        assert len(components) == 1
        assert set(components[0]) == {'A', 'B', 'C', 'D'}

    def test_wcc_two_components(self):
        """Test WCC with two separate components."""
        g = DirectedGraph()
        # Component 1
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')

        # Component 2
        g.add_edge('D', 'E')
        g.add_edge('E', 'F')

        components = g.weakly_connected_components()

        assert len(components) == 2
        component_sets = [set(c) for c in components]
        assert {'A', 'B', 'C'} in component_sets
        assert {'D', 'E', 'F'} in component_sets

    def test_wcc_isolated_vertices(self):
        """Test WCC with isolated vertices."""
        g = DirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        components = g.weakly_connected_components()

        assert len(components) == 3
        assert all(len(c) == 1 for c in components)

    def test_wcc_with_cycle(self):
        """Test WCC with a cycle (should still be one component)."""
        g = DirectedGraph()

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')

        components = g.weakly_connected_components()

        assert len(components) == 1
        assert set(components[0]) == {'A', 'B', 'C'}

    def test_wcc_mixed_components(self):
        """Test WCC with mix of connected and isolated vertices."""
        g = DirectedGraph()

        # Connected component
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')

        # Isolated vertices
        g.add_vertex('D')
        g.add_vertex('E')

        components = g.weakly_connected_components()

        assert len(components) == 3
