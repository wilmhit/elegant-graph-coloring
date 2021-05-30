from typing import cast

from minizinc import Instance, Model, Solver, Status

from .custom_types import AdjMatrix
from .config import BASE_DIR


def elegantly_color_edges(graph: AdjMatrix) -> AdjMatrix:
    """Return an adjacency matrix represnting elegantly colored edges."""
    model_path = BASE_DIR.joinpath("models/elegant_labeling.mzn")
    model = Model(model_path)
    instance = Instance(Solver.lookup("gecode"), model)
    instance["graph"] = graph
    instance["total_edges"] = sum(row.count(1) for row in graph) // 2
    instance["total_vertices"] = len(graph)
    result = instance.solve()
    if (status := result.status) != Status.SATISFIED:
        error = f"An error occured when coloring the graph. Returned status: {status}"
        raise RuntimeError(error)
    return cast(AdjMatrix, result["coloring"])
