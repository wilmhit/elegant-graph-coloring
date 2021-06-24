from .custom_types import AdjMatrix

def count_edges(graph: AdjMatrix) -> int:
    return sum(sum(element > 0 for element in row) for row in graph) // 2
