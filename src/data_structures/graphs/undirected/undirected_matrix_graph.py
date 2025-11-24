class UndirectedMatrixGraph:
    """
    Implements an Undirected Weighted Graph using an Adjacency Matrix.
    Edges are stored symmetrically. Uses None to represent absence of edges.

    Space Complexity: O(V²) where V is the number of vertices
    """

    def __init__(self, num_vertices):
        """
        Initialize graph with given number of vertices.

        Time Complexity: O(V²) for matrix initialization

        Args:
            num_vertices: Number of vertices in the graph

        Raises:
            ValueError: If num_vertices <= 0
        """
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive")

        self.num_vertices = num_vertices
        self.matrix = [[None] * num_vertices for _ in range(num_vertices)]

    def add_edge(self):
        pass

    def remove_edge(self):
        pass

    def has_edge(self):
        pass

    def get_weight(self):
        pass

    def get_neighbors(self):
        pass

    def get_degree(self):
        pass

    def get_all_edges(self):
        pass

    def _is_valid_vertex(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
