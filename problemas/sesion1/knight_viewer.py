from typing import TextIO
import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.viewers.graph2d_viewer import Graph2dViewer

from knight import knight_graph


type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int, int, int]
type Result = tuple[UndirectedGraph[Vertex], int]

def read_data(f: TextIO) -> Data:
    n_rows,n_cols = tuple(int(s) for s in f.readline().split())
    return n_rows, n_cols

def process(data: Data) -> Result:
    n_rows, n_cols = data
    return knight_graph(n_rows, n_cols)

def show_result(result : Result):
    g = result
    gv = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
    gv.run()

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)