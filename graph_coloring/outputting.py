from typing import List, Any, Tuple, Dict

import networkx
from matplotlib import pyplot

from .custom_types import AdjMatrix

Edge = Tuple[int, int]


def get_edges_and_labels(graph: AdjMatrix) -> Tuple[List[Edge], Dict[Edge, int]]:
    edges: List[Edge] = []
    labels: Dict[Edge, int] = {}
    for row_num, row in enumerate(graph):
        for column_num, element in enumerate(row):
            if column_num < row_num:
                continue
            if element:
                edge = (row_num, column_num)
                edges.append(edge)
                labels[edge] = element

    return edges, labels


def output_results(colored_edges: AdjMatrix, colored_vertices: List[int]) -> None:
    edges, labels = get_edges_and_labels(colored_edges)
    graph = networkx.Graph()
    graph.add_nodes_from(colored_vertices)
    graph.add_edges_from(edges)
    layout = networkx.spring_layout(graph)

    networkx.draw_networkx_nodes(graph, layout)
    networkx.draw_networkx_edges(graph, layout)
    networkx.draw_networkx_labels(graph, layout)
    networkx.draw_networkx_edge_labels(graph, layout, edge_labels=labels)
    pyplot.tight_layout(pad=0)
    pyplot.show()
