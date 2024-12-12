# https://adventofcode.com/2024/day/6
# --- Day 6: Guard Gallivant ---

from copy import deepcopy
from sys import setrecursionlimit, stdin

setrecursionlimit(10**5)


def find_guard(puzzle: list[list[str]]) -> tuple[int, int]:
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == "^":
                return x, y
    return -1, -1


def solution1(puzzle: list[list[str]]) -> int:
    def _go_guard(x: int, y: int, dx: int, dy: int):
        if x < 0 or x >= len(puzzle[0]) or y < 0 or y >= len(puzzle):
            return
        if puzzle[y][x] == "#":
            _go_guard(x - dx, y - dy, -dy, dx)
            return
        puzzle[y][x] = "X"
        _go_guard(x + dx, y + dy, dx, dy)
        return

    x0, y0 = find_guard(puzzle)
    puzzle = deepcopy(puzzle)
    _go_guard(x0, y0, 0, -1)

    cntr = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "X":
                cntr += 1

    return cntr


def solution2(puzzle: list[list[str]]) -> int:
    def _go_guard_cycle(x: int, y: int, dx: int, dy: int) -> bool:
        while 0 <= x < len(puzzle[0]) and 0 <= y < len(puzzle):
            if puzzle[y][x] == "#":
                x -= dx
                y -= dy
                dx, dy = -dy, dx
            else:
                cell = x, y, dx, dy
                if cell in visited:
                    return True
                visited.add(cell)
                x += dx
                y += dy

        return False

    x0, y0 = find_guard(puzzle)
    visited = set()
    _go_guard_cycle(x0, y0, 0, -1)

    obstacles = set((x, y) for x, y, *_ in visited)
    obstacles.remove((x0, y0))
    cntr = 0
    for x, y in obstacles:
        puzzle[y][x] = "#"
        visited.clear()
        if _go_guard_cycle(x0, y0, 0, -1):
            cntr += 1
        puzzle[y][x] = "."

    return cntr


puzzle = [list(line[:-1]) for line in stdin]
print(solution1(puzzle))
print(solution2(puzzle))
