class DirectedMatrixGraph:
    """
      Implements a Directed Weighted Graph using an Adjacency Matrix.
      Edges are stored non-symmetrically with support for negative weights.
      Uses None to represent absence of edges (allowing zero-weight edges).
    """

    def __init__(self, num_vertices):
        """
        Initialize a directed weighted graph with num_vertices vertices.

        Time Complexity: O(V²) where V is the number of vertices
        Space Complexity: O(V²) for the adjacency matrix
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

    def get_in_degree(self):
        pass

    def get_out_degree(self):
        pass

    def display_matrix(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
