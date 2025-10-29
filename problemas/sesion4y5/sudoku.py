import sys
from typing import TextIO, Iterator

from problemas.sesion4y5.auxiliares4_5.sudoku_lib import from_strings

type Sudoku = list[list[int]]
type Data = Sudoku
type Result = Iterator[Sudoku]

def read_data(f: TextIO) -> Data:
    return from_strings(f.readlines())

def process(data:Data) -> Result:


def show_result(result: Result):
    pass

if __name__ == "main":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)

