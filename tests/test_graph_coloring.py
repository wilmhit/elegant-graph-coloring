import pytest

from graph_coloring.custom_types import AdjMatrix
from graph_coloring.coloring import elegantly_color
from .sample_graphs import SHACK_F_4, DI_3, STAR_S_6


def assert_colored_elegantly(edges: AdjMatrix, vertices: list) -> None:
    edges_colors = [color for row in edges for color in row if color != 0]
    total_edges_colors_assigned = len(edges_colors) // 2
    vertices_set = set(vertices)
    edges_set = set(edges_colors)

    # Edges should be a set with values in range [1; total_edges]
    assert len(edges_set) == total_edges_colors_assigned
    assert max(edges_set) <= total_edges_colors_assigned
    assert min(edges_set) >= 1

    # Vertices should be a set with values in range [0; total_edges]
    assert len(vertices) == len(vertices_set)
    assert max(vertices_set) <= total_edges_colors_assigned
    assert min(vertices_set) >= 0

    for i, row in enumerate(edges):
        for j in range(len(row)):
            if color := edges[i][j]:
                # Edge colors should be distinct values obtained by the following formula
                assert edges_colors.count(color) == 2  # Two because adjacency matrix
                assert color == (vertices[i] + vertices[j]) % (
                    total_edges_colors_assigned + 1
                )


@pytest.mark.parametrize(
    "graph",
    [
        (
            [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
            ]
        ),
        (
            [
                [0, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 1, 0, 0],
            ]
        ),
        STAR_S_6["graph"],
        SHACK_F_4["graph"],
        DI_3["graph"],
    ],
)
def test_graph_colored_correctly(graph: AdjMatrix):
    assert_colored_elegantly(*elegantly_color(graph))


@pytest.mark.parametrize(
    "graph_with_more_vertices_than_edges",
    [
        [
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 0],
        ],
    ],
)
def test_error_raised_when_graph_unsatisfiable(
    graph_with_more_vertices_than_edges: AdjMatrix,
):
    with pytest.raises(RuntimeError):
        elegantly_color(graph_with_more_vertices_than_edges)
