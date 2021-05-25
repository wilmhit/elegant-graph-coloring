from custom_types import Graph


def graph_from_string(graph_file: str) -> Graph:
    """
        The string should represent an adjacency matrix, separated with spaces and "\n",
        ```
        0 1 \n
        1 0 \n
        ```
    """
    return [to_cells(line_str) for line_str in graph_file.split("\n")]


def to_cells(line: str) -> list[int]:
    cells = line.split(" ")
    cells = list(filter(lambda cell: cell != "", cells))
    return [int(cell) for cell in cells]