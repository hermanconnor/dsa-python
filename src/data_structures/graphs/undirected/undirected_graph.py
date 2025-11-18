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

    def is_empty(self) -> bool:
        """
        Check if the graph has any vertices.

        Time Complexity: O(1)
        """
        return len(self.graph) == 0

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
