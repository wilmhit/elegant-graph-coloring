# Elegant graph coloring (labeling).

*An elegant labeling f of a graph G with m edges is an injective function from the
vertices of G to the set {0, 1, 2, . . . , m} such that when each edge x y is assigned the
label f(x) + f(y)(mod m + 1), the resulting edge labels are distinct and nonzero.*

A. Elumalai and G. Sethuraman "Elegant Labeled Graphs"
## Running

Install python and then do:
```
$ git clone https://github.com/wilmhit/elegant-graph-coloring.git
$ cd elegant-graph-coloring
$ python -m pip install pipenv
$ chmod +x run.sh
$ ./run.sh <Input graph file>
```

## Examples

Few sample graphs are located in `graphs` dir.

## Contributing

Open pull request.

## Based on

G. J. Chang, D. F. Hsu, and D. G. Rogers, Additive variations on a graceful theme:
some results on harmonious and other related graphs, Congr. Numer., 32 (1981)
181-197

Graph Labeling
Joseph A. Gallian
2018-12-15
116-118
Available [here](https://www.combinatorics.org/ojs/index.php).
