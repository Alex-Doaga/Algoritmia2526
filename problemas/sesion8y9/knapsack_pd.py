from typing import TextIO
import sys

type Score = int
type Decision = int
type Solution = tuple[Score, list[Decision]|None]

type Data = tuple[int, list[int], list[int]]
type Result = Solution

type SParams = tuple[int, int]

type Mem = dict[SParams, Score]
type MemSolution = dict[SParams, tuple[Score, SParams, Decision]]



def read_data(f: TextIO) -> Data:
    C = int(f.readline())
    v = []
    w = []
    for line in f.readlines():
        p = line.strip().split()
        v.append(int(p[0]))
        w.append(int(p[1]))
    return C, v, w


def process_direct(data: Data) -> Result:
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0
        if  w[n -1] > c:
            return S(c, n-1)
        else:
            return max(S(C, n-1), S(c - w[n - 1], n - 1) + v[n -1])

    C,v,w = data
    score = S(C, len(v))
    return score, None


def process_memo(data: Data) -> Result:
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0
        if (c, n) not in mem:
            if  w[n -1] > c:
                mem[c, n] = S(c, n-1)
            else:
                mem[c, n] = max(S(C, n-1), S(c - w[n - 1], n - 1) + v[n -1])

        return mem[c, n]

    C,v,w = data
    mem: Mem = {}                               #type Mem = dict[SParams, Score]
    score = S(C, len(v))
    return score, None

### EXAMENNNNNNNNNNNNNNNNNNNNN programar 0'75 puntos
### COSTE decir coste 0'5 puntos

# Coste espacial O (C* N)
# Coste temporal O (C * N)
# Pseudopolinómico en C

def process_memo_solution(data: Data) -> Result:
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0
        if (c, n) not in mem:
            if w[n - 1] > c:
                mem[c, n] = S(c, n - 1), (c, n - 1), 0
            else:
                mem[c, n] = max((S(c, n - 1), (c, n - 1), 0),
                                (S(c - w[n - 1], n - 1) + v[n - 1], (c - w[n -1], n -1),1))

        return mem[c, n][0]

    C, v, w = data
    mem: MemSolution = {}  # type MemSolution = dict[SParams, tuple[Score, SParams, Decision]]
    score = S(C, len(v))
    decisions = []
    c,n = C, len(v)
    while n > 0:
        _, (c, n), d = mem[c,n]
        decisions.append(d)
    decisions.reverse()

    return score, decisions

### NO ENTRA EN EL EXAMENNNNNNNNNN
def process_iter(data: Data) -> Result:

    C, v, w = data
    mem: MemSolution = {}  # type MemSolution = dict[SParams, tuple[Score, SParams, Decision]]

    for c in range(C + 1):
        mem[c, 0] = 0, (-1, -1), -1
    for n in range(1, len(v) + 1):
        for c in range (C + 1):
            if w[n - 1] > c:
                mem[c, n] = mem[c, n - 1][0], (c, n - 1), 0
            else:
                mem[c, n] = max((mem[c, n - 1][0], (c, n - 1), 0),
                                (mem[c - w[n - 1], n - 1][0] + v[n - 1], (c - w[n -1], n -1),1))

    score = mem[C, len(v)][0]
    decisions = []
    c,n = C, len(v)
    while n > 0:
        _, (c, n), d = mem[c,n]
        decisions.append(d)
    decisions.reverse()

    return score, decisions

### NO ENTRA EN EL EXAMENNNNNNNNNN
def process_iter_red(data: Data) -> Result:

    C, v, w = data
    previous = [0] * (C +1)
    current = [0] *  (C + 1)

    for n in range(1, len(v) + 1):
        current, previous = previous, current
        for c in range (C + 1):
            if w[n - 1] > c:
                current[c] = previous[c]
            else:
                current[c] = max(previous[c,],
                                previous[c - w[n - 1]] + v[n - 1])

    score = current[C]
    return score, None

def show_result(result: Result):
    tv, decisions = result
    print(tv)
    if decisions is not None:
        for d in decisions:
            print(d)


if __name__ == "__main__":
    # process = process_direct
    # process = process_memo
    #process = process_memo_solution
    process = process_iter
    # process = process_iter_red
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
