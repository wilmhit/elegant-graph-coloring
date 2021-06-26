from typing import Callable, Dict, List, Set, Tuple

import networkx
from matplotlib import pyplot

from .custom_types import AdjMatrix
from .graph_utils import enumerate_half_graph, print_graph_info

Edge = Tuple[int, int]
EdgeLabels = Dict[Edge, int]


def get_edges_and_labels(
    graph: AdjMatrix, labels_of_vertices: List[int]
) -> Tuple[List[Edge], EdgeLabels]:
    edges: List[Edge] = []
    labels: EdgeLabels = {}

    for color, row, col in enumerate_half_graph(graph):
        if color:
            edge = (labels_of_vertices[row], labels_of_vertices[col])
            edges.append(edge)
            labels[edge] = color
    return edges, labels


def output_results(colored_graph: AdjMatrix, vertex_labels: List[int]) -> None:
    edges, edge_labels = get_edges_and_labels(colored_graph, vertex_labels)
    graph = networkx.Graph()
    graph.add_nodes_from(vertex_labels)
    graph.add_edges_from(edges)
    layout = networkx.spring_layout(graph)

    print_graph_info(colored_graph)

    networkx.draw_networkx_nodes(graph, layout)
    networkx.draw_networkx_edges(graph, layout)
    networkx.draw_networkx_labels(graph, layout)
    networkx.draw_networkx_edge_labels(graph, layout, edge_labels=edge_labels)

    pyplot.tight_layout(pad=0)
    pyplot.show()
