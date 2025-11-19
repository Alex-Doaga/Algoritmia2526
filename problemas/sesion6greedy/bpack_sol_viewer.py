import sys
from typing import Dict, TextIO


type Weight = int
type BinNumber = int
type Bin = list[Weight]


def read_weights(name) -> tuple[Weight, list[Weight]]:
    f = open(name)
    C = int(f.readline())
    return C, [int(i) for i in f.readlines()]


def read_data(f: TextIO) -> list[BinNumber]:
    return [int(i) for i in f.readlines()]


def process(C: Weight, bin_numbers: list[BinNumber], weights: list[Weight]) -> list[Bin]:
    d: Dict[int, list[int]] = {}
    for it, p in enumerate(bin_numbers):
        if p not in d:
            d[p] = []
        d[p].append(weights[it])
    r = [sorted(d[p]) for p in sorted(d.keys())]
    for b in r:
        if sum(b) > C:
            sys.stderr.write(f"Error: la solución no es válida: bin {b}\n")
            sys.exit(1)
    return r


def show_results(bins: list[Bin]):
    for i, b in enumerate(bins):
        print(f"{i:3}: {', '.join(str(it) for it in b)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Error: necesito exactamente un parámetro, el nombre el fichero del problema")
        sys.exit(1)
    C, weights = read_weights(sys.argv[1])
    bin_numbers = read_data(sys.stdin)
    bins = process(C, bin_numbers, weights)
    show_results(bins)

