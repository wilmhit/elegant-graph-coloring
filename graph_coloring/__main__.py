import argparse
from sys import exit
from argparse import Namespace

from .file_operations import get_graph_string
from .graph_parsing import graph_from_string
from .coloring import elegantly_color
from .graph_validation import get_error_if_invalid
from .outputting import output_results


def main(args: Namespace) -> None:
    graph_str = get_graph_string(args.GRAPH)
    graph = graph_from_string(graph_str)

    if error := get_error_if_invalid(graph):
        exit(error)

    output_results(*elegantly_color(graph))


parser = argparse.ArgumentParser()
parser.add_argument("GRAPH", type=str, help="Text file containing graph")

main(parser.parse_args())
