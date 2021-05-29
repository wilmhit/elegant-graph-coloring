from .custom_types import AdjMatrix
from pathlib import Path
from minizinc import Instance, Model, Solver, Status


def get_colored_edges(graph: AdjMatrix) -> AdjMatrix:
    """Return an adjacency matrix represnting elegantly colored edges."""
    model_path = Path(__file__).parent.absolute().joinpath("models/elegant_labeling.mzn")
    model = Model(model_path)
    instance = Instance(Solver.lookup("gecode"), model)
    instance["graph"] = graph
    instance["total_edges"] = sum(row.count(1) for row in graph) // 2
    instance["total_vertices"] = len(graph)
    result = instance.solve()
    if (status := result.status) != Status.SATISFIED:
        error_message = f"An error occured when coloring the graph. Returned status: {status}"
        raise RuntimeError(error_message)
    return result["coloring"]  # type: ignore
