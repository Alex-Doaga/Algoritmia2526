import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from labyrinth import create_labyrinth

type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int]
type Result = tuple[UndirectedGraph[Vertex],
list[Vertex]]


def bf_search(g: UndirectedGraph[Vertex],
source: Vertex, target: Vertex) -> list[Edge]:

    queue: Fifo[Vertex] = Fifo()
    seen: set[Vertex] = {source}
    edges: list[Edge] = [(source,source)]

    queue.push(source)

    while len(queue) > 0:
        u = queue.pop()
        if u == target:
            break
        for v in g.succs(u):
            if v not in seen:
                seen.add(v)
                queue.push(v)
                edges.append((u,v))

    return edges

def path_recover(edges: list[Edge],target: Vertex) -> list[Vertex]:
    #Construir bp
    bp: dict[Vertex,Vertex] = {}
    for (u, v) in edges:
        bp[v] = u


    #Usar bp para recuperar el camino
    v = target
    path = [v]

    while bp[v] != v:
        v = bp[v]
        path.append(v)

    path.reverse()
    return path

def read_data(f: TextIO) -> Data:
    n_rows,n_cols = tuple(int(s) for s in f.readline().split())
    return n_rows, n_cols

def process(data: Data) -> Result:
    n_rows, n_cols = data
    lab = create_labyrinth(n_rows,n_cols)
    source = 0,0
    target = n_rows -1, n_cols -1
    edges = bf_search(lab,source,target)
    path = path_recover(edges, target)
    return lab, path

def show_result(result : Result):
    lab,path = result
    for (r, c ) in path:
        print(r,c)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)