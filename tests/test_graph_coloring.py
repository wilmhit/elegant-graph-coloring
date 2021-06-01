import pytest

from graph_coloring.custom_types import AdjMatrix
from graph_coloring.coloring import elegantly_color_edges
from .sample_graphs import SHACK_F_4, DI_3, STAR_S_6


@pytest.mark.parametrize(
    "graph, expected_coloring",
    [
        (
            [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
            ],
            [
                [0, 1, 2],
                [1, 0, 3],
                [2, 3, 0],
            ],
        ),
        (
            [
                [0, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 1, 0, 0],
            ],
            [
                [0, 1, 2, 3],
                [1, 0, 0, 4],
                [2, 0, 0, 0],
                [3, 4, 0, 0],
            ],
        ),
        (
            STAR_S_6["graph"],
            STAR_S_6["coloring"],
        ),
        (
            SHACK_F_4["graph"],
            SHACK_F_4["coloring"],
        ),
        (
            DI_3["graph"],
            DI_3["coloring"],
        ),
    ],
)
def test_graph_colored_correctly(graph: AdjMatrix, expected_coloring: AdjMatrix):
    assert elegantly_color_edges(graph) == expected_coloring


@pytest.mark.parametrize(
    "non_colorable_graph",
    [
        [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ],
    ],
)
def test_error_raised_when_graph_could_not_be_solved(non_colorable_graph: AdjMatrix):
    with pytest.raises(RuntimeError):
        elegantly_color_edges(non_colorable_graph)
