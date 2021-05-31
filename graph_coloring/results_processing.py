from custom_types import AdjMatrix
import networkx
from matplotlib import pyplot
from typing import List, Any, Tuple


def get_node_array(graph: AdjMatrix) -> List[int]:
    return [x for x in range(len(graph))]


def get_edge_array(graph: AdjMatrix) -> List[Tuple[int, int, Any]]:
    edges = []
    for row_num, row in enumerate(graph):
        for column_num, element in enumerate(row):
            if column_num < row_num:
                continue
            if element:
                edges.append((row_num, column_num, {"weight": element}))
    return edges


def output_results(results: AdjMatrix) -> None:
    graph = networkx.Graph()
    graph.add_nodes_from(get_node_array(results))
    graph.add_edges_from(get_edge_array(results))
    networkx.draw_spring(graph)
    pyplot.show()
