# https://adventofcode.com/2024/day/15
# --- Day 15: Warehouse Woes ---

from copy import deepcopy
from sys import stdin


def find_robot(grid: list[list[str]]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return j, i
    return -1, -1


def count_gps(grid: list[list[str]], box: str) -> int:
    gps = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == box:
                gps += 100 * i + j

    return gps


DXDY = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def solution1(grid: list[str], moves: str) -> int:
    grid = [list(line) for line in grid]
    x, y = find_robot(grid)
    for m in moves:
        dx, dy = DXDY[m]
        x_next = x + dx
        y_next = y + dy

        if grid[y_next][x_next] == "O":
            x_empty, y_empty = x_next, y_next
            while grid[y_empty][x_empty] == "O":
                x_empty += dx
                y_empty += dy
            if grid[y_empty][x_empty] == ".":
                grid[y_empty][x_empty] = "O"
                grid[y_next][x_next] = "."

        if grid[y_next][x_next] == ".":
            grid[y][x] = "."
            grid[y_next][x_next] = "@"
            x, y = x_next, y_next

    return count_gps(grid, "O")


def solution2(grid: list[str], moves: str) -> int:
    def _make_grid() -> list[list[int]]:
        new_grid = []
        for line in grid:
            line = (
                line.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            new_grid.append(list(line))

        return new_grid

    def _move_x(x: int, y: int, dx: int):
        x_empty = x
        while grid[y][x_empty] in "[]":
            x_empty += dx
        if grid[y][x_empty] == ".":
            while x_empty != x:
                grid[y][x_empty] = grid[y][x_empty - dx]
                x_empty -= dx
            grid[y][x] = "."

    def _move_y(x: int, y: int, dy: int, grid: list[list[str]]) -> bool:
        if x <= 1 or x >= len(grid[0]) - 2 or y <= 0 or y >= len(grid) - 1:
            return False
        if grid[y][x] == "#":
            return False
        if grid[y][x] == ".":
            return True

        y_next = y + dy
        x_pair = x - 1 if grid[y][x] == "]" else x + 1
        if _move_y(x, y_next, dy, grid) and _move_y(x_pair, y_next, dy, grid):
            grid[y_next][x] = grid[y][x]
            grid[y_next][x_pair] = grid[y][x_pair]
            grid[y][x] = grid[y][x_pair] = "."
            return True
        return False

    grid = _make_grid()
    x, y = find_robot(grid)
    for m in moves:
        dx, dy = DXDY[m]
        x_next = x + dx
        y_next = y + dy

        if grid[y_next][x_next] in "[]":
            if dy == 0:
                _move_x(x_next, y_next, dx)
            else:
                tmp = deepcopy(grid)
                if _move_y(x_next, y_next, dy, tmp):
                    grid = tmp

        if grid[y_next][x_next] == ".":
            grid[y][x] = "."
            grid[y_next][x_next] = "@"
            x, y = x_next, y_next

    return count_gps(grid, "[")


grid, moves = stdin.read().split("\n\n")
grid = [line for line in grid.split()]
moves = moves.replace("\n", "")

print(solution1(grid, moves))
print(solution2(grid, moves))
