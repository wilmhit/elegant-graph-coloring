from .custom_types import AdjMatrix

def count_edges(graph: AdjMatrix) -> int:
    count_non_zero = lambda row: sum(element > 0 for element in row)
    return sum(count_non_zero(row) for row in graph) // 2
