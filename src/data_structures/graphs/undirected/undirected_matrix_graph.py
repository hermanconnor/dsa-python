class UndirectedMatrixGraph:
    """
    Implements an Undirected Weighted Graph using an Adjacency Matrix.
    Edges are stored symmetrically with support for negative weights.
    Uses None to represent absence of edges (allowing zero-weight edges).
    """

    def __init__(self, num_vertices):
        """
        Initialize an undirected weighted graph with num_vertices vertices.
        Time Complexity: O(V²) where V is the number of vertices
        Space Complexity: O(V²) for the adjacency matrix
        """
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive")

        self.num_vertices = num_vertices
        self.matrix = [[None] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        """
        Adds a weighted edge BETWEEN u and v (symmetric).
        Time Complexity: O(1)
        """
        self._validate_vertices(u, v)
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def remove_edge(self, u, v):
        """
        Removes the edge BETWEEN u and v (both directions).
        Time Complexity: O(1)
        Returns: True if edge was removed, False if no edge existed
        """
        self._validate_vertices(u, v)

        if self.matrix[u][v] is not None:
            self.matrix[u][v] = None
            self.matrix[v][u] = None
            return True
        return False

    def has_edge(self, u, v):
        """
        Checks if an edge exists BETWEEN u and v.
        Time Complexity: O(1)
        """
        self._validate_vertices(u, v)
        return self.matrix[u][v] is not None

    def get_weight(self, u, v):
        """
        Returns the weight of edge between u and v, or None if no edge exists.
        Time Complexity: O(1)
        """
        self._validate_vertices(u, v)
        return self.matrix[u][v]

    def get_neighbors(self, u):
        """
        Returns a list of (vertex, weight) tuples for all edges connected to u.
        Time Complexity: O(V) where V is the number of vertices
        """
        self._validate_vertex(u)
        return [(v, self.matrix[u][v]) for v in range(self.num_vertices)
                if self.matrix[u][v] is not None]

    def get_degree(self):
        pass

    def get_all_edges(self):
        pass

    def _validate_vertex(self, v):
        """Validates a single vertex index."""
        if not (0 <= v < self.num_vertices):
            raise IndexError(
                f"Vertex {v} out of bounds [0, {self.num_vertices})")

    def _validate_vertices(self, u, v):
        """Validates two vertex indices."""
        self._validate_vertex(u)
        self._validate_vertex(v)

    def __str__(self):
        """String representation showing edge list."""
        edges = []
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):  # Avoid duplicates
                if self.matrix[u][v] is not None:
                    edges.append(f"{u} --({self.matrix[u][v]})-- {v}")
        return f"UndirectedMatrixGraph({self.num_vertices} vertices, {len(edges)} edges)\n" + \
               "\n".join(
                   edges) if edges else f"UndirectedMatrixGraph({self.num_vertices} vertices, 0 edges)"

    def __repr__(self):
        return f"UndirectedMatrixGraph(num_vertices={self.num_vertices})"
