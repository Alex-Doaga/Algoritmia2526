from typing import TextIO
import sys

type Decision = int
type Score = int
type Solution = tuple[int, list[int]|None]

type SParams = tuple[int, int]
type Mem = dict[SParams, Score]
type MemSolution = dict[SParams, tuple[Score, Decision]]

type Data = tuple[int, int, list[int], list[int], list[int]]
type Result = Solution | None


infinity = 10**100


def read_data(f: TextIO) -> Data:
    N = int(f.readline())
    Q = int(f.readline())
    v = [int(w) for w in f.readline().split()]
    w = [int(w) for w in f.readline().split()]
    m = [int(w) for w in f.readline().split()]
    return N, Q, v, w, m


def process_direct(data: Data) -> Result:
    raise NotImplementedError


def process_memo(data: Data) -> Result:
    raise NotImplementedError


def process_memo_solution(data: Data) -> Result:
    raise NotImplementedError


def process_iter(data: Data) -> Result:
    raise NotImplementedError


def process_iter_red(data: Data) -> Result:
    raise NotImplementedError


def show_result(result: Result):
    if result is None:
        print("No solution")
        return
    s, ds = result
    print(s)
    if ds is not None:
        for d in ds:
            print(d)


if __name__ == "__main__":
    process = process_direct
    # process = process_memo
    # process = process_memo_solution
    # process = process_iter
    # process = process_iter_red
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
