#!/usr/bin/env python3
import sys
from typing import TextIO

type Data = list[int]
type Result = bool

def read_data(f: TextIO) -> Data:
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]

def process(data: Data) -> Result:
    seen = set()

    for n in data:
        if n in seen:
            return True
        seen.add(n)
    return False

def show_result(result: Result):
    # Escribir el resultado
    print("No hay repetidos" if not result
          else "Hay repetidos")

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
