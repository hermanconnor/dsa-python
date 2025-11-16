from __future__ import annotations
from collections import defaultdict, deque
from typing import (
    Any, Dict, List, Optional, Set, Tuple,
    TypeVar, Hashable, Generic, Deque
)

V = TypeVar('V', bound=Hashable)
W = TypeVar('W', bound=Any)


class DirectedGraph(Generic[V, W]):
    """
      A directed graph implementation with optional edge weights.
      Uses adjacency list representation for efficiency.
      """

    def __init__(self) -> None:
        """
        Initialize an empty directed graph.

        Time Complexity: O(1)
        """
        self.graph: Dict[V, List[Tuple[V, W]]] = defaultdict(list)
        self.in_degree_counts: Dict[V, int] = defaultdict(int)

    def add_vertex(self, vertex: V) -> None:
        """
        Add a vertex to the graph if it doesn't exist.

        Time Complexity: O(1)
        """
        if vertex not in self.graph:
            self.graph[vertex]

        if vertex not in self.in_degree_counts:
            self.in_degree_counts[vertex] = 0

    def add_edge(self, from_vertex: V, to_vertex: V, weight: W = 1) -> bool:
        """
        Add a directed edge from from_vertex to to_vertex.
        Prevents duplicate edges between the same vertices.

        Time Complexity: O(E_v) where E_v is the out-degree of from_vertex
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        # Check for duplicate edge (O(E_v))
        if any(neighbor == to_vertex for neighbor, _ in self.graph[from_vertex]):
            return False

        # Add the edge
        self.graph[from_vertex].append((to_vertex, weight))
        self.in_degree_counts[to_vertex] += 1

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

        # 1. Remove all outgoing edges and update in-degrees of neighbors
        for neighbor, _ in self.graph[vertex]:
            if neighbor in self.in_degree_counts:
                self.in_degree_counts[neighbor] -= 1

        # 2. Remove all edges pointing *to* this vertex, and update in-degrees of this vertex
        vertices_to_check = list(self.graph.keys())
        for v in vertices_to_check:
            # Skip the vertex being removed, which will be deleted in the next step
            if v == vertex:
                continue

            self.graph[v] = [
                (neighbor, weight) for neighbor, weight in self.graph[v] if neighbor != vertex
            ]

        # 3. Remove the vertex from the graph and in_degrees
        del self.graph[vertex]
        del self.in_degree_counts[vertex]

        return True

    def remove_edge(self, from_vertex: V, to_vertex: V) -> bool:
        """
        Remove the directed edge from from_vertex to to_vertex.

        Time Complexity: O(E_v) where E_v is the number of edges from from_vertex

        Returns:
            bool: True if edge was removed, False if it didn't exist
        """
        if from_vertex not in self.graph:
            return False

        original_length = len(self.graph[from_vertex])

        # Rebuild the list without the target edge
        self.graph[from_vertex] = [
            (neighbor, weight) for neighbor, weight in self.graph[from_vertex] if neighbor != to_vertex
        ]

        # Update in-degree count only if an edge was actually removed
        if len(self.graph[from_vertex]) < original_length:
            if to_vertex in self.in_degree_counts:
                self.in_degree_counts[to_vertex] -= 1

            return True

        return False

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
        Get all edges as a list of (from, to, weight) tuples.

        Time Complexity: O(V + E)
        """
        edges = []

        for from_vertex in self.graph:
            for to_vertex, weight in self.graph[from_vertex]:
                edges.append((from_vertex, to_vertex, weight))

        return edges

    def has_edge(self, from_vertex: V, to_vertex: V) -> bool:
        """
        Check if there's a directed edge from from_vertex to to_vertex.

        Time Complexity: O(E_v) where E_v is the number of edges from from_vertex
        """
        if from_vertex not in self.graph:
            return False

        return any(neighbor == to_vertex for neighbor, _ in self.graph[from_vertex])

    def get_edge_weight(self, from_vertex: V, to_vertex: V) -> Optional[W] | None:
        """
        Get the weight of the edge from from_vertex to to_vertex.

        Time Complexity: O(E_v) where E_v is the number of edges from from_vertex

        Returns:
            weight or None: Weight if edge exists, None otherwise
        """
        if from_vertex in self.graph:
            for neighbor, weight in self.graph[from_vertex]:
                if neighbor == to_vertex:
                    return weight

        return None

    def update_edge_weight(self, from_vertex: V, to_vertex: V, new_weight: W) -> bool:
        """
        Update the weight of an existing edge.

        Time Complexity: O(E_v) where E_v is the number of edges from from_vertex

        Returns:
            bool: True if edge was updated, False if edge doesn't exist
        """
        if from_vertex in self.graph:
            for i, (neighbor, _) in enumerate(self.graph[from_vertex]):
                if neighbor == to_vertex:
                    self.graph[from_vertex][i] = (neighbor, new_weight)
                    return True

        return False

    def in_degree(self, vertex: V) -> int:
        """
        Calculate the in-degree of a vertex (number of incoming edges).

        Time Complexity: O(1)

        Raises:
            ValueError: If vertex not in graph
        """
        if vertex not in self.graph:
            raise ValueError(f"Vertex {vertex} not in graph")

        return self.in_degree_counts[vertex]

    def out_degree(self, vertex: V) -> int:
        """
        Calculate the out-degree of a vertex (number of outgoing edges).

        Time Complexity: O(1)

        Raises:
            ValueError: If vertex not in graph
        """
        if vertex not in self.graph:
            raise ValueError(f"Vertex {vertex} not in graph")

        return len(self.graph[vertex])

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

    def has_cycle(self):
        pass

    def topological_sort(self):
        pass

    def reverse(self):
        pass

    def strongly_connected_components(self):
        pass

    def weakly_connected_components(self):
        pass

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
        self.in_degree_counts.clear()

    def copy(self):
        pass

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
                    f"{neighbor}({weight})" for neighbor, weight in neighbors]

                result.append(f"{vertex} -> {', '.join(neighbor_strs)}")
            else:
                result.append(f"{vertex} -> []")

        return "\n".join(result)

    def __repr__(self) -> str:
        """
        Unambiguous representation of the graph.

        Time Complexity: O(1)
        """
        num_vertices = len(self.graph)
        num_edges = sum(len(edges) for edges in self.graph.values())

        return f"DirectedGraph(vertices={num_vertices}, edges={num_edges})"
