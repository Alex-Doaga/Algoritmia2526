from typing import TextIO
import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from shortest_path import bf_search


type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int, int, int]
type Result = tuple[UndirectedGraph[Vertex], int]

def knight_graph(n_rows: int, n_cols: int) -> UndirectedGraph[Vertex]:
    #Lista de vértices
    vertices: list[Vertex] = [(r,c) for r in range(n_rows) for c in range(n_cols)]
    #lista de aristas
    edges : list[Edge] = []
    for (r, c) in vertices:
        for(ir, ic) in [(1,-2),(2,-1),(2,1),(1,2)]:
            r2 = r+ir
            c2 = c+ic
            if 0 <= r2 < n_rows and 0 <= c2 < n_cols:
                edges.append(((r, c), (r2, c2)))
    return UndirectedGraph(V=vertices, E = edges)



def read_data(f: TextIO) -> Data:
    n_rows,n_cols = tuple(int(s) for s in f.readline().split())
    pos_r, pos_c =tuple(int(s) for s in f.readline().split())
    return n_rows, n_cols, pos_r, pos_c

def process(data: Data) -> Result:
    n_rows, n_cols, pos_r, pos_c = data
    g = knight_graph(n_rows, n_cols)
    edges = bf_search(g,(0,0),(-1,-1))
    vertices_count = len(edges)
    return g, len(edges)

def show_result(result : Result):
    g,vertices_count = result
    print(vertices_count)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)