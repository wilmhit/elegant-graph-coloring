from custom_types import Graph as AdjMatrix
import networkx
from matplotlib import pyplot

def get_node_array(graph: AdjMatrix):
    return [x for x in range(len(graph))]

def get_edge_array(graph: AdjMatrix):
    return [(1,2)] # TODO

def output_results(results: AdjMatrix) -> None:
    graph = networkx.Graph()
    graph.add_nodes_from(get_node_array(results))
    graph.add_edges_from(get_edge_array(results))
    networkx.draw(graph)
    pyplot.show()
