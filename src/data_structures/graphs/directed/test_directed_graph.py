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
