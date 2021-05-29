import pytest

from graph_coloring.custom_types import AdjMatrix
from graph_coloring.coloring import get_colored_edges
from graph_coloring.sample_graphs import SHAK_F_4, DI_3, STAR_S_6


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
            SHAK_F_4["graph"],
            SHAK_F_4["coloring"],
        ),
        (
            DI_3["graph"],
            DI_3["coloring"],
        ),
    ],
)
def test__graph__colored_correctly(graph: AdjMatrix, expected_coloring: AdjMatrix):
    assert get_colored_edges(graph) == expected_coloring


@pytest.mark.parametrize(
    "invalid_graph",
    [
        [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ],
    ],
)
def test_error_raised_when_graph_could_not_be_solved(invalid_graph: AdjMatrix):
    with pytest.raises(RuntimeError):
        get_colored_edges(invalid_graph)