from typing import List, Tuple, cast

from minizinc import Instance, Model, Solver, Status

from .config import MIZNIZIC_MODELS_DIR
from .custom_types import AdjMatrix
from .graph_utils import count_edges


def elegantly_color(graph: AdjMatrix) -> Tuple[AdjMatrix, List[int]]:
    """Return an adjacency matrix represnting elegantly colored edges."""
    model_path = MIZNIZIC_MODELS_DIR.joinpath("elegant_labeling.mzn")
    model = Model(model_path)
    instance = Instance(Solver.lookup("gecode"), model)

    instance["graph"] = graph
    instance["total_edges"] = count_edges(graph)
    instance["total_vertices"] = len(graph)

    result = instance.solve()
    if (status := result.status) != Status.SATISFIED:
        error = f"An error occured when coloring the graph. Returned status: {status}"
        raise RuntimeError(error)
    return cast(AdjMatrix, result["colored_edges"]), result["colored_vertices"]
