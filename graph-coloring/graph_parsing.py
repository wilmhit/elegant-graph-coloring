from types import Graph


def parse_graph_file(graph_file: str) -> Graph:
    """
    Parses string into graph. String must be separated with spaces and \n
    """

    graph = []
    lines = split_lines(graph_file)
    for line in lines:
        cells = split_spaces(line)
        cells = remove_empty_cells(cells)
        graph.append(parse_into_numbers(cells))
    return graph


def split_lines(graph_file: str) -> list[str]:
    return graph_file.split("\n")


def split_spaces(line: str) -> list[str]:
    return line.split(" ")


def remove_empty_cells(cells: list[str]) -> list[str]:
    return list(filter(lambda cell: cell != "", cells))


def parse_into_numbers(cells: list[str]) -> list[int]:
    return [int(cell) for cell in cells]
