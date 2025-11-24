from __future__ import annotations
from collections import defaultdict, deque
from typing import (
    Any, Dict, List, Optional, Set, Tuple,
    TypeVar, Hashable, Generic, Deque
)

V = TypeVar('V', bound=Hashable)
W = TypeVar('W', bound=Any)


class UndirectedGraph(Generic[V, W]):
    """
    An undirected graph implementation with optional edge weights.
    Uses adjacency list representation for efficiency.
    """

    def __init__(self) -> None:
        """
        Initialize an empty undirected graph.

        Time Complexity: O(1)
        """
        self.graph: Dict[V, List[Tuple[V, W]]] = defaultdict(list)

    def add_vertex(self, vertex: V) -> None:
        """
        Add a vertex to the graph if it doesn't exist.

        Time Complexity: O(1)
        """
        if vertex not in self.graph:
            self.graph[vertex]

    def add_edge(self, vertex1: V, vertex2: V, weight: W = 1) -> bool:
        """
        Add an undirected edge between vertex1 and vertex2.
        Prevents duplicate edges and self-loops.

        Time Complexity: O(E_v) where E_v is the degree of the vertices
        """

        # Prevent self-loops
        if vertex1 == vertex2:
            return False

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Check for duplicate edge (O(E_v))
        if any(neighbor == vertex2 for neighbor, _ in self.graph[vertex1]):
            return False

        # Add edge in both directions
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

        return True

    def remove_vertex(self, vertex: V) -> bool:
        """
        Remove a vertex and all edges connected to it.

        Time Complexity: O(V + E) where V is vertices and E is edges

        Returns:
            bool: True if vertex was removed, False if it didn't exist
        """
        if vertex not in self.graph:
            return False

        # Remove all edges from neighbors pointing to this vertex
        for neighbor, _ in self.graph[vertex]:
            if neighbor in self.graph:
                self.graph[neighbor] = [
                    (v, w) for v, w in self.graph[neighbor] if v != vertex
                ]
        # Remove the vertex from the graph
        del self.graph[vertex]

        return True

    def remove_edge(self, vertex1: V, vertex2: V) -> bool:
        """
        Remove the undirected edge between vertex1 and vertex2.

        Time Complexity: O(E_v) where E_v is the degree of the vertices

        Returns:
            bool: True if edge was removed, False if it didn't exist
        """
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False

        original_length1 = len(self.graph[vertex1])
        original_length2 = len(self.graph[vertex2])

        # Remove edge from both directions
        self.graph[vertex1] = [
            (neighbor, weight) for neighbor, weight in self.graph[vertex1]
            if neighbor != vertex2
        ]

        self.graph[vertex2] = [
            (neighbor, weight) for neighbor, weight in self.graph[vertex2]
            if neighbor != vertex1
        ]

        # Check if edge was actually removed
        edge_removed = (len(self.graph[vertex1]) < original_length1 and
                        len(self.graph[vertex2]) < original_length2)

        return edge_removed

    def get_neighbors(self, vertex: V) -> List[Tuple[V, W]]:
        """
        Get all neighbors of a vertex with their weights.

        Time Complexity: O(1)

        Raises:
            ValueError: If vertex not in graph
        """
        if vertex not in self.graph:
            raise ValueError(f"Vertex {vertex} not in graph")

        return self.graph[vertex]

    def get_vertices(self) -> List[V]:
        """
        Get all vertices in the graph.

        Time Complexity: O(V)
        """
        return list(self.graph.keys())

    def get_edges(self) -> List[Tuple[V, V, W]]:
        """
        Get all edges as a list of (vertex1, vertex2, weight) tuples.
        Each edge appears only once.

        Time Complexity: O(V + E)
        """
        edges = []
        seen = set()

        for vertex1 in self.graph:
            for vertex2, weight in self.graph[vertex1]:
                # Use frozenset to avoid duplicate edges
                edge = frozenset([vertex1, vertex2])
                if edge not in seen:
                    seen.add(edge)
                    edges.append((vertex1, vertex2, weight))

        return edges

    def has_edge(self, vertex1: V, vertex2: V) -> bool:
        """
        Check if there's an edge between vertex1 and vertex2.

        Time Complexity: O(E_v) where E_v is the degree of vertex1
        """
        if vertex1 not in self.graph:
            return False

        return any(neighbor == vertex2 for neighbor, _ in self.graph[vertex1])

    def get_edge_weight(self, vertex1: V, vertex2: V) -> W | None:
        """
        Get the weight of the edge between vertex1 and vertex2.

        Time Complexity: O(E_v) where E_v is the degree of vertex1

        Returns:
            weight or None: Weight if edge exists, None otherwise
        """
        if vertex1 in self.graph:
            for neighbor, weight in self.graph[vertex1]:
                if neighbor == vertex2:
                    return weight

        return None

    def update_edge_weight(self, vertex1: V, vertex2: V, new_weight: W) -> bool:
        """
        Update the weight of an existing edge in both directions.

        Time Complexity: O(E_v) where E_v is the degree of the vertices

        Returns:
            bool: True if edge was updated, False if edge doesn't exist
        """
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False

        updated = False

        # Update in both directions
        for i, (neighbor, _) in enumerate(self.graph[vertex1]):
            if neighbor == vertex2:
                self.graph[vertex1][i] = (neighbor, new_weight)
                updated = True
                break

        if updated:
            for i, (neighbor, _) in enumerate(self.graph[vertex2]):
                if neighbor == vertex1:
                    self.graph[vertex2][i] = (neighbor, new_weight)
                    break

        return updated

    def degree(self, vertex: V) -> int:
        """
        Calculate the degree of a vertex (number of edges connected to it).

        Time Complexity: O(1)

        Raises:
            ValueError: If vertex not in graph
        """
        if vertex not in self.graph:
            raise ValueError(f"Vertex {vertex} not in graph")

        return len(self.graph[vertex])

    def copy(self) -> 'UndirectedGraph[V, W]':
        """
        Create a deep copy of the graph.

        Time Complexity: O(V + E)
        """
        new_graph = UndirectedGraph()

        # Add all vertices
        for vertex in self.graph:
            new_graph.add_vertex(vertex)

        # Add all edges (each edge appears twice in adjacency list)
        seen = set()
        for vertex1 in self.graph:
            for vertex2, weight in self.graph[vertex1]:
                edge = frozenset([vertex1, vertex2])
                if edge not in seen:
                    seen.add(edge)
                    new_graph.add_edge(vertex1, vertex2, weight)

        return new_graph

    def dfs(self, start_vertex: V) -> List[V]:
        """
        Depth-First Search traversal starting from start_vertex (iterative).
        Returns list of vertices in DFS order.

        Time Complexity: O(V + E)

        Raises:
            ValueError: If start_vertex not in graph
        """
        if start_vertex not in self.graph:
            raise ValueError(f"Vertex {start_vertex} not in graph")

        visited: Set[V] = set()
        stack = [start_vertex]
        result = []

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Add neighbors in reverse to maintain left-to-right order
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def bfs(self, start_vertex: V) -> List[V]:
        """
        Breadth-First Search traversal starting from start_vertex.
        Returns list of vertices in BFS order.

        Time Complexity: O(V + E)

        Raises:
            ValueError: If start_vertex not in graph
        """
        if start_vertex not in self.graph:
            raise ValueError(f"Vertex {start_vertex} not in graph")

        visited: Set[V] = set()
        queue: Deque[V] = deque([start_vertex])
        result = []

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor, _ in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def is_empty(self) -> bool:
        """
        Check if the graph has any vertices.

        Time Complexity: O(1)
        """
        return len(self.graph) == 0

    def clear(self) -> None:
        """
        Remove all vertices and edges from the graph.

        Time Complexity: O(1)
        """
        self.graph.clear()

    def __contains__(self, vertex: V) -> bool:
        """
        Check if a vertex is in the graph. Allows 'if vertex in graph:'.

        Time Complexity: O(1)
        """
        return vertex in self.graph

    def __str__(self) -> str:
        """
        String representation of the graph showing adjacency lists.

        Time Complexity: O(V + E)
        """
        if not self.graph:
            return "Empty Graph"

        result = []
        for vertex in sorted(self.graph.keys(), key=str):
            neighbors = self.graph[vertex]

            if neighbors:
                neighbor_strs = [
                    f"{neighbor}({weight})" for neighbor, weight in neighbors
                ]

                result.append(f"{vertex} -- {', '.join(neighbor_strs)}")
            else:
                result.append(f"{vertex} -- []")

        return "\n".join(result)

    def __repr__(self) -> str:
        """
        Unambiguous representation of the graph.

        Time Complexity: O(1)
        """
        num_vertices = len(self.graph)
        # Each edge is stored twice, so divide by 2
        num_edges = sum(len(edges) for edges in self.graph.values()) // 2

        return f"UndirectedGraph(vertices={num_vertices}, edges={num_edges})"
