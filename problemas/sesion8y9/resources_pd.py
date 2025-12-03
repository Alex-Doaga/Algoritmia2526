from typing import TextIO
import sys

from problemas.sesion8y9.coinchange_pd import infinity

type Score = int
type Decision = int
type Solution = tuple[Score, list[Decision]|None]

type Data = tuple[int, int, list[int], list[list[Score]]]
type Result = Solution

type SParams = tuple[int, int]
type Mem = dict[SParams, Score]
# type MemSolution = dict[SParams, tuple[Score, Decision]]
type MemSolution = dict[SParams, tuple[Score, SParams, Decision]]

def read_data(f: TextIO) -> Data:
    U = int(f.readline())
    N = int(f.readline())
    m = [int(w) for w in f.readline().split()]
    v = [[int(w) for w in l.split()] for l in f.readlines()]
    return U, N, m, v


def process_direct(data: Data) -> Solution:
    def S(u, n):
        if n == 0:
            return 0

        # Código avanzado
        g = (S(u-d, n-1) + v[n - 1][d] for d in range (min(m[n -1], u) + 1))
        return max(g)

        # Código clásico

        # best_score = -infinity
        # for d in range (min(m[n -1], u) + 1):
        #     current_score = S(u -d, n - 1) + v[n - 1][d]
        #     best_score = max(best_score, current_score)
        #
        # return best_score

    U, N, m, v = data
    score = S(U, N)
    return score, None

def process_memo(data: Data) -> Solution:
    def S(u, n):
        if n == 0:
            return 0

        if (u, n) not in mem:   # <-- Nuevo
            g = (S(u - d, n - 1) + v[n - 1][d] for d in range(min(m[n - 1], u) + 1))
            mem[u, n] = max(g)

        return mem[u, n]

    U, N, m, v = data
    mem: Mem = {}
    score = S(U, N)
    return score, None

def process_memo_solution(data: Data) -> Solution:
    def S(u, n):
        if n == 0:
            return 0

        if (u, n) not in mem:
            g = ((S(u - d, n - 1) + v[n - 1][d], (u - d, n - 1),d) for d in range(min(m[n - 1], u) + 1))
            mem[u, n] = max(g)

        return mem[u, n][0]

    U, N, m, v = data
    mem: MemSolution = {}
    score = S(U, N)
    decisions = []
    u, n = U, N
    while n > 0:
        _,(u, n), d = mem[u, n]
        decisions.append(d)
    decisions.reverse()
    return score,decisions

def process_iter(data: Data) -> Solution:
    raise NotImplementedError


def process_iter_red(data: Data) -> Solution:
    raise NotImplementedError

def show_result(result: Result):
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
