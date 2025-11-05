from collections.abc import Iterator, Iterable


type Position = tuple[int, int]
type Sudoku = list[list[int]]


def empty_cells(s: Sudoku) -> Iterator[Position]:
    for row in range(9):
        for col in range(9):
            if s[row][col] == 0:
                yield row, col


def first_empty(s: Sudoku) -> Position | None:
    return next(empty_cells(s), None)


def allowed(s: Sudoku, pos: Position) -> set[int]:
    row, col = pos
    fc, cc = row // 3 * 3, col // 3 * 3
    used = ({s[row][c] for c in range(9)}
            | {s[f][col] for f in range(9)}
            | {s[fc + f][cc + c]
               for f in range(3)
               for c in range(3)})
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, row in enumerate(s):
        for j, column in enumerate(row):
            print(column if column != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


def from_strings(strings: Iterable[str]) -> Sudoku:
    return [[int(c) if c != '.' else 0 for c in string.strip()]
            for string in strings]
