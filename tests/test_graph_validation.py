import pytest
from graph_coloring.custom_types import AdjMatrix
from graph_coloring.graph_validation import edges_greater_equal_vertices

@pytest.mark.parametrize(
	"graph",
	[
		[
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
	]
)
def test_edge_counting_passing(graph: AdjMatrix):
    assert edges_greater_equal_vertices(graph)


@pytest.mark.parametrize(
	"graph",
	[
		[
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
	]
)
def test_edge_counting_failing(graph: AdjMatrix):
    assert not edges_greater_equal_vertices(graph)
