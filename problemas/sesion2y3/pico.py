from typing import TextIO

from algoritmia.schemes.dac_scheme import div_solve

type Data = list[int]
type Result = int

def read_data(f: TextIO) -> Data:
    data = []
    for line in f:
        data.append(int(line))
    return data

def process (data:Data) -> Result:
    start = 0
    end = len(data)

    # while is_simple
    while end - start > 1:
        #decrease
        mid = (start + end) // 2
        if data[mid - 1] < data[mid]:
            start = mid
        else:
            end = mid
    return data[start]

def show_result (result: Result):
    print(result)
