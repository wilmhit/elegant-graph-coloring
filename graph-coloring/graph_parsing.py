from custom_types import Graph


def graph_from_string(graph_str: str) -> Graph:
    """
    The string should represent an adjacency matrix, separated with spaces and \\n.

    Example:
    \n0 1 1\n1 0 1\n1 1 0
    """
    graph_str = graph_str.strip()
    return [to_cells(line_str) for line_str in graph_str.split("\n")]


def to_cells(line: str) -> list[int]:
    cells = line.split(" ")
    cells = list(filter(lambda cell: cell != "", cells))
    return [int(cell) for cell in cells]
