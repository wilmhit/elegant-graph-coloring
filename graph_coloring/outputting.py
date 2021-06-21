from typing import List, Tuple, Dict, Set

import networkx
from json import dumps
from matplotlib import pyplot

from .custom_types import AdjMatrix
from .graph_utils import pretty_print_graph

Edge = Tuple[int, int]


def get_edges_and_labels(graph: AdjMatrix, vertex_labels: List[int]) -> Tuple[List[Edge], Dict[Edge, int]]:
    edges: Set[Edge] = set()
    labels: Dict[Edge, int] = {}
    indexes_to_vertex_labels = lambda i1, i2: (vertex_labels[i1],
                                               vertex_labels[i2])
    for from_ver_num, row in enumerate(graph):
        for to_ver_num, edge_value in enumerate(row):
            if edge_value:
                lower_vertex = min(from_ver_num,to_ver_num)
                higer_vertex = max(from_ver_num, to_ver_num)
                edge = indexes_to_vertex_labels(lower_vertex, higer_vertex)
                edges.add(edge)
                labels[edge] = edge_value
    return list(edges), labels


def output_results(colored_graph: AdjMatrix, vertex_labels: List[int]) -> None:
    edges, edge_labels = get_edges_and_labels(colored_graph, vertex_labels)
    graph = networkx.Graph()
    graph.add_nodes_from(vertex_labels)
    graph.add_edges_from(edges)
    layout = networkx.spring_layout(graph)

    networkx.draw_networkx_nodes(graph, layout)
    networkx.draw_networkx_edges(graph, layout)
    networkx.draw_networkx_labels(graph, layout)
    networkx.draw_networkx_edge_labels(graph, layout, edge_labels=edge_labels)

    pyplot.tight_layout(pad=0)
    pyplot.show()
