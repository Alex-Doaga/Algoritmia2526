import sys
from dataclasses import dataclass
from typing import TextIO, Iterator, Self

from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solutions, min_solution, bt_vc_solutions, State

type Data = tuple[int, list[int]]
type Result = list[int] | None          # la lista es de elementos de e
type Decision = int                     # 0 o 1

def read_data(f: TextIO) -> Data:
    s = int(f.readline())
    e = [ int(line) for line in f]

    return s,e

# Backtracking (Búsqueda con retroceso) Versión más lenta
def process_simple(data: Data) -> Result:

    s,e = data

    @dataclass
    class Extra:
        suma: int

    class SubsetSumDS(DecisionSequence[Decision,Extra]):
        def is_solution(self) -> bool:
            return len(self) == len(e) and self.extra.suma == s

        def successors(self) -> Iterator[Self]:
            n = len(self)
            if n < len(e):          #Solo generamos sucesores si quedan decisiones por tomar

                suma_actual = self.extra.suma + e[n]
                if suma_actual <= s:
                    yield self.add_decision(1, Extra(suma_actual))
                yield self.add_decision(0,self.extra)

    def f(decisions: tuple[Decision, ...]) -> int:
        return sum(decisions)


    initial_ds = SubsetSumDS(Extra(0))
    all_sols = [sol_ds.decisions() for sol_ds in bt_solutions(initial_ds)]
    best_sol = min_solution(all_sols, f)

    if best_sol is None:
        return None

    score, decisions = best_sol
    nums = [e[i] for i,d in enumerate(decisions) if d == 1]

    return nums

# Backtracking con control de visitados Versión más rápida. Coge la primera solución posible
def process_state(data: Data) -> Result:

    s,e = data

    @dataclass
    class Extra:
        suma: int

    class SubsetSumDS(DecisionSequence[Decision,Extra]):
        def is_solution(self) -> bool:
            return len(self) == len(e) and self.extra.suma == s

        def successors(self) -> Iterator[Self]:
            n = len(self)
            if n < len(e):          #Solo generamos sucesores si quedan decisiones por tomar

                suma_actual = self.extra.suma + e[n]
                if suma_actual <= s:
                    yield self.add_decision(1, Extra(suma_actual))
                yield self.add_decision(0,self.extra)

        def state(self) -> State:                                  #NUEVO
            return len(self), self.extra.suma                      #NUEVO

    def f(decisions: tuple[Decision, ...]) -> int:
        return sum(decisions)


    initial_ds = SubsetSumDS(Extra(0))
    all_sols = [sol_ds.decisions() for sol_ds in bt_vc_solutions(initial_ds)]       #MODIFICAR
    best_sol = min_solution(all_sols, f)

    if best_sol is None:
        return None

    score, decisions = best_sol
    nums = [e[i] for i,d in enumerate(decisions) if d == 1]

    return nums

# Backtracking con control de visitados con la mejor solución. Versión rápida pero coge la mejor solución
def process_full_state(data: Data) -> Result:

    s,e = data

    @dataclass
    class Extra:
        suma: int
        num_unos: int           #Numeros usados

    class SubsetSumDS(DecisionSequence[Decision,Extra]):
        def is_solution(self) -> bool:
            return len(self) == len(e) and self.extra.suma == s

        def successors(self) -> Iterator[Self]:
            n = len(self)
            if n < len(e):          #Solo generamos sucesores si quedan decisiones por tomar

                suma_actual = self.extra.suma + e[n]
                if suma_actual <= s:
                    yield self.add_decision(1, Extra(suma_actual,self.extra.num_unos + 1))   #MODIFICADO
                yield self.add_decision(0,self.extra)

        def state(self) -> State:                                                    #NUEVO
            return len(self), self.extra.suma, self.extra.num_unos                   #MODIFICADO

    def f(decisions: tuple[Decision, ...]) -> int:
        return sum(decisions)


    initial_ds = SubsetSumDS(Extra(0,0))                                            #MODIFICADO
    all_sols = [sol_ds.decisions() for sol_ds in bt_vc_solutions(initial_ds)]       #MODIFICADO
    best_sol = min_solution(all_sols, f)

    if best_sol is None:
        return None

    score, decisions = best_sol
    nums = [e[i] for i,d in enumerate(decisions) if d == 1]

    return nums

def show_result(result: Result):
    if result is None:
        print("No hay solucion")
    else:
        for el in result:
            print(el)


if __name__ == '__main__':

    data0 = read_data(sys.stdin)
    result0 = process_full_state(data0)
    show_result(result0)
