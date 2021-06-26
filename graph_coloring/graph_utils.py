from typing import Generator, Tuple

from .custom_types import AdjMatrix


def count_edges(graph: AdjMatrix) -> int:
    return sum(sum(element > 0 for element in row) for row in graph) // 2


def enumerate_half_graph(graph: AdjMatrix) -> Generator[Tuple[int, int, int], None, None]:
    """Yields tuple `(value, row, column)`"""
    for row_num in range(len(graph)):
        for col_num in range(row_num, len(graph)):
            value = graph[row_num][col_num]
            yield value, row_num, col_num


def print_graph_info(graph: AdjMatrix) -> None:
    print("Total edges: ", count_edges(graph))
    print("Total vertices: ", len(graph))
