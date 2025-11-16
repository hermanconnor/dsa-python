from collections import defaultdict, deque
from typing import (
    Any, Dict, List, Optional, Set, Tuple,
    TypeVar, Hashable, Generic, cast
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
        self.in_degrees: Dict[V, int] = defaultdict(int)

    def add_vertex(self, vertex: V) -> None:
        """
        Add a vertex to the graph if it doesn't exist.

        Time Complexity: O(1)
        """
        pass

    def add_edge(self, from_vertex: V, to_vertex: V, weight: W = 1) -> bool:
        """
        Add a directed edge from from_vertex to to_vertex.
        Prevents duplicate edges between the same vertices.

        Time Complexity: O(E_v) where E_v is the out-degree of from_vertex
        """
        pass

    def remove_vertex(self):
        pass

    def remove_edge(self):
        pass

    def get_neighbors(self):
        pass

    def get_vertices(self):
        pass

    def get_edges(self):
        pass

    def has_edge(self):
        pass

    def get_edge_weight(self):
        pass

    def update_edge_weight(self):
        pass

    def in_degree(self):
        pass

    def out_degree(self):
        pass

    def dfs(self):
        pass

    def bfs(self):
        pass

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

    def is_empty(self):
        pass

    def clear(self):
        pass

    def copy(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
