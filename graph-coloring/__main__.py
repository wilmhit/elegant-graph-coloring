import argparse
from argparse import Namespace
from file_operations import get_graph_file, save_png
from graph_parsing import graph_from_string
from custom_types import Graph, Idk


def main(args: Namespace) -> None:
    graph_str = get_graph_file(args.GRAPH)
    graph = graph_from_string(graph_str)
    output = process_graph(graph)
    save_png(output, args.out)


def process_graph(graph: Graph) -> Idk:
    pass


parser = argparse.ArgumentParser()
parser.add_argument('GRAPH', type=str, help="Text file containing graph")
parser.add_argument('-f',
                    '--out',
                    type=str,
                    help="Output file",
                    default="output.png")

main(parser.parse_args())
