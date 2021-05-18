import argparse
from argparse import Namespace
from file_operations import get_graph_file, save_png
from graph_parsing import parse_graph_file


def main(args: Namespace):
    graph_file = get_graph_file(args.GRAPH)
    graph = parse_graph_file(graph_file)
    output = process_graph(graph)
    save_png(output, args.out)


def process_graph(graph) -> None:
    pass


parser = argparse.ArgumentParser()
parser.add_argument('GRAPH', type=str, help="Text file containing graph")
parser.add_argument('-f',
                    '--out',
                    type=str,
                    help="Output file",
                    default="output.png")

main(parser.parse_args())
