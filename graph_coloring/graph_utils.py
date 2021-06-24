from .custom_types import AdjMatrix
from typing import Tuple

def count_edges(graph: AdjMatrix) -> int:
    return sum(sum(element > 0 for element in row) for row in graph) // 2

def enumerate_half_graph(graph: AdjMatrix) -> Tuple[int, int, int]:
    """ Yields tuple `(value, row, column)` """
    for row_num in range(len(graph)):
        for col_num in range(row_num, len(graph)):
            value = graph[row_num][col_num]
            yield value, row_num, col_num
