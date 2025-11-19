import sys
from typing import TextIO

type Data = tuple[int, list[int]]
type Result = list[int]

def read_data(f: TextIO) -> Data:
    cap = int(f.readline())
    pesos = [int(linea) for linea in f]
    return cap,pesos

def process_mq(data: Data) -> Result:
    c, w = data
    res = [-1] * len(w)
    cw = 0
    nc = 0

    for i, w in enumerate(w):           # enumerate devuelve el indice y el elemento de una lista
        if cw + w > c:
            nc += 1
            cw = 0
        cw += w
        res[i] = nc

    return res


def process_pqq(data: Data) -> Result:
    c, W = data
    res = [-1] * len(W)
    cws = [0] * len(W)                   #Pesos actuales de los contenedores

    for i,w in enumerate(W):
        for nc, cw in enumerate(cws):
            if cw + w <= c:
                res[i] = nc
                cws[nc] += w
                break
    return res

def process_pqqo(data: Data) -> Result:
    c, W = data
    res = [-1] * len(W)
    cws = [0] * len(W)                  #Pesos actuales de los contenedores

    indices = list(range(len(W)))
    sorted_indices = sorted(indices, key = lambda i: W[i], reverse = True)
    for i in sorted_indices:            #antes obteniamos juntos i, w
        w = W[i]                        #ahora solo i, obtenemos w
        for nc, cw in enumerate(cws):
            if cw + w <= c:
                res[i] = nc
                cws[nc] += w
                break

    return res

def show_results(result: Result):
    for nCont in result:
        print(nCont)

if __name__ == "__main__":
    # process = process_mq
    #process = process_pqq
    process = process_pqqo

    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_results(result0)

