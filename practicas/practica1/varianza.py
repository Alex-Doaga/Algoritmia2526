#!/usr/bin/env python3
import sys
from typing import TextIO

type Data = list[int]
type Result = float

def read_data(f: TextIO) -> Data:
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]

def average(nums: list[int]) -> float:
    return sum(nums)/len(nums)

def process(data: Data) -> Result:
    s = 0
    av = average(data)
    for num in data:
        s += (num - av) ** 2
    return s/len(data)

def show_result(result: Result):
    # Escribir el resultado
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
