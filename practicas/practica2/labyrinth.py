import random
import sys
from random import shuffle
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

type Data = tuple[int, int]    # ( num_rows, num_cols)
type Vertex = tuple[int, int]  # (row,col)
type Edge = tuple[Vertex, Vertex]  # ((row1, col1), (row2, col2))
type Result = UndirectedGraph[Vertex]

def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols

def process(data: Data) -> Result:

    #Paso 1
    num_rows, num_cols = data
    vertices: list[Vertex] = []

    for row in range(num_rows):
        for col in range(num_cols):
            vertices.append((row,col))

    #Otra forma de hacerlo más breve vertices = [(row,col) for row in range(num_rows) for col in range(num_cols)]

    #Paso 2
    mfs = MergeFindSet()
    for vertice in vertices:
        mfs.add(vertice)

    #Paso 3
    edges: list[Edge] = []
    for r,c in vertices:
        if r+1 < num_rows:
            edges.append(((r,c), (r+1,c)))
        if c+1 < num_cols:
            edges.append(((r,c), (r,c+1)))

    shuffle(edges)

    #Paso 4
    corridors: list[Edge] = []

    #Paso 5
    for u,v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            corridors.append((u, v))

    #Paso 6
    return UndirectedGraph(E=corridors)

def show_result(result: Result):
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)