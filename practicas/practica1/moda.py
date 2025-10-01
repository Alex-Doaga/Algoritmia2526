#!/usr/bin/env python3
import sys
from typing import TextIO

type Data = list[int]
type Result = int

def read_data(f: TextIO) -> Data:
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(data: Data) -> Result:
    dic: dict[int,int] = {}
    mas_visto = -1
    veces_visto = 0
    for num in data:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

        if(dic[num] > veces_visto):
            veces_visto = dic[num]
            mas_visto = [num]

    return mas_visto



def show_result(result: Result):
    # Escribir el resultado
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
