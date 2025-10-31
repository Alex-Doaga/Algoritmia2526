import sys
from copy import deepcopy
from locale import normalize
from typing import TextIO, Iterator, Self

from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solutions

from problemas.sesion4y5.auxiliares4_5.sudoku_lib import from_strings, Position, pretty_print, first_empty, allowed, \
    empty_cells

type Sudoku = list[list[int]]
type Data = Sudoku
type Result = Iterator[Sudoku]
type Decision = tuple[Position, int]
type Extra = None

def read_data(f: TextIO) -> Data:
    return from_strings(f.readlines())

def process_slow(data:Data) -> Result:
    class Extra:
        sudoku: Sudoku

    class SudokuDS(DecisionSequence[Decision, Extra]):
        def is_solution(self) -> bool:
            return first_empty(self.extra.sudoku) is None

        def successors(self) -> Iterator[Self]:
            # averigua primera posición vacía
            pos = first_empty(self.extra.sudoku)

            if ( pos is not None ):
                #crea un hijo para cada numero 'allowed' en esa posicion
             for num in allowed(self.extra.sudoku, pos):
                # El hijo necesita un nuevo self.extra.sudoku para no modificar el del padre.
                new_sudoku = deepcopy(self.extra.sudoku)
                #quitamos el cero de pos poniendo num
                new_sudoku[r][c] = num
                #generamos el hijo (un nuevo SudokuDS )
                d = (pos, num)
                yield solution_ds.decisions(d, Extra(new_sudoku))

    initial_sudoku = data
    initial_ds = SudokuDS(Extra(initial_sudoku))
    for solution_ds in bt_solutions(initial_ds):
        yield solution_ds.decisions()

def process_fast(data:Data) -> Result:
    class Extra:
        sudoku: Sudoku
        empty: set[Position]

    class SudokuDS(DecisionSequence[Decision, Extra]):
        def is_solution(self) -> bool:
            return len(self.extra.empty) == 0

        def successors(self) -> Iterator[Self]:
            if len(self.extra.empty) > 0:
                best_allowed = None
                best_pos = None
                for pos in self.extra.empty:
                    current_allowed = allowed(self.extra.sudoku, pos)
                    if best_allowed is None or len(best_allowed) > len(current_allowed):
                            best_allowed = current_allowed
                            best_pos = pos
                    r, c = best_pos
                    for num in best_allowed:
                        # El hijo necesita un nuevo self.extra.sudoku para no modificar el del padre.
                        # quitamos el cero de pos poniendo num
                        self.new_sudoku[r][c] = num
                        self.new_empty.remove(best_pos)
                        # generamos el hijo (un nuevo SudokuDS )
                        d = (best_pos, num)
                        yield self.add_decision(d, self.extra)

    initial_sudoku = data
    vacais_iniciales = set(empty_cells(initial_sudoku))
    initial_ds = SudokuDS(Extra(initial_sudoku))
    for solution_ds in bt_solutions(initial_ds):
        yield solution_ds.decisions()


def show_result(result: Result):
    for sudoku in result:
        pretty_print(sudoku)

if __name__ == "main":
    process = process_fast()
    # process = process_slow()
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)

