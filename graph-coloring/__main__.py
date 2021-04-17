import argparse
from files import *

parser = argparse.ArgumentParser()
parser.add_argument('GRAPH', type=str, help="Text file containing graph")
parser.add_argument('-f',
                    '--out',
                    type=str,
                    help="Output file",
                    default="output.png")

main(parser.parse_args())

def main(args):
    graph_file = get_graph_file(args.GRAPH)
    output = process_graph(graph_file)
    save_png(output, args.out)
