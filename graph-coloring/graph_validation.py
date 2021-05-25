from typing import Optional
from custom_types import Graph

def get_error(graph: Graph) -> Optional[str]:
    """Retruns user-friendly error message or None"""
    if not is_square(graph):
        return "This graph has not square"
    if not has_zeros_on_diagonal(graph):
        return "Diagonal must consist only of zeros"
    return None

def is_square(graph: Graph) -> bool:
    side_lenght = len(graph)
    for line in graph:
        if len(line) != side_lenght:
            return False
    return True

def has_zeros_on_diagonal(graph: Graph) -> bool:
    for x in range(len(graph)):
        if graph[x][x] != 0:
            return False
    return True
