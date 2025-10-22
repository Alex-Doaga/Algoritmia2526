import sys
from typing import TextIO

from algoritmia.schemes.dac_scheme import div_solve, IDivideAndConquerProblem
from algoritmia.utils import infinity

type Data = list[int]               #Lista no ordenada de positivos y negativos
type Result = tuple[int, int, int]  # (suma_del_subvector, indice_inicio_subvector, indice_final_subvector[FUERA)

def read_data(f: TextIO) -> Data:
    data = []
    for line in f:
        data.append(int(line))
    return data

# usa una estrategia de “divide y vencerás” para encontrar el subvector de suma máxima
def process(data:Data) -> Result:
    def rec(b: int, e: int) -> Result:
        # if is_simple
        if e - b == 1:
            # return trivial_solution
            return data[b],b,e
        else:
            # divide (y la recursividad)
            mid = (b + e) // 2
            best_left = rec(b,mid)
            best_right = rec(mid,e)

            # combine
            # Mejor indice derecha(e2)
            e2 = -1
            acc = 0
            best_acc_right = -infinity
            for i in range(mid,e):
                acc += data[i]
                if acc > best_acc_right:
                    best_acc_right = acc
                    e2 = i + 1

            # Mejor indice izquierda (b2)
            b2 = -1
            acc = 0
            best_acc_left = -infinity
            for i in range(mid - 1, b - 1, -1): # for al revés. El b - 1 es para que llegue a b ( No se pare en el de antes )
                acc += data[i]
                if acc > best_acc_left:
                    best_acc_left = acc
                    b2 = i #

            best_mid = (best_acc_left + best_acc_right, b2, e2 )

            return max(best_left, best_mid, best_right)

    return rec(0,len(data))

# Escribe por pantalla tres valores, uno por línea: la suma del subvector y los valores de b y e
def show_result(result: Result):
    suma_subvector, b, e = result
    print(suma_subvector)
    print(b)
    print(e)

if __name__ == "main":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)

