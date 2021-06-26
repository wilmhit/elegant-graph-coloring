from typing import Optional

from .custom_types import AdjMatrix
from .graph_utils import count_edges


def get_error_if_invalid(graph: AdjMatrix) -> Optional[str]:
    """Error messages are descriptive and user-friendly."""

    if not is_square(graph):
        return "The provided graph is not square"
    if not has_zeros_on_diagonal(graph):
        return "The provided graph should only have zeros on its diagonal"
    if not edges_greater_equal_vertices(graph):
        return "The provided graph must have more edges than vertices"
    return None


def is_square(graph: AdjMatrix) -> bool:
    side_lenght = len(graph)
    return all(len(row) == side_lenght for row in graph)


def has_zeros_on_diagonal(graph: AdjMatrix) -> bool:
    return all(graph[x][x] == 0 for x in range(len(graph)))


def edges_greater_equal_vertices(graph: AdjMatrix) -> bool:
    vertices = len(graph)
    edges = count_edges(graph)
    return edges >= vertices - 1
