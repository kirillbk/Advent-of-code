# https://adventofcode.com/2024/day/20
# --- Day 20: Race Condition ---

from collections.abc import Generator
from sys import setrecursionlimit, stdin

setrecursionlimit(10**5)


def find_cell(grid: list[str], cell: str) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == cell:
                return j, i
    return -1, -1


def get_track(grid: list[str]) -> dict[tuple[int, int], int]:
    def _get_track(x: int, y: int, t: int):
        track[(x, y)] = t
        if grid[y][x] == "E":
            return
        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if grid[to_y][to_x] in ".E" and (to_x, to_y) not in track:
                _get_track(to_x, to_y, t + 1)

    x, y = find_cell(grid, "S")
    track = dict()
    _get_track(x, y, 0)

    return track


def solution1(grid: list[str]) -> int:
    def _cheats(x0: int, y0: int) -> Generator[tuple[int, int]]:
        dx, dy = 0, 1
        for _ in range(4):
            x1 = x0 + 2 * dx
            y1 = y0 + 2 * dy
            if (
                0 <= x1 < len(grid[0])
                and 0 <= y1 < len(grid)
                and grid[y1][x1] in ".ES"
                and grid[y0 + dy][x0 + dx] == "#"
                and track[(x0, y0)] + 2 < track[(x1, y1)]
            ):
                yield x1, y1
            dx, dy = -dy, dx

    track = get_track(grid)
    cntr = 0
    for x0, y0 in track:
        for x1, y1 in _cheats(x0, y0):
            if track[(x0, y0)] + 2 <= track[(x1, y1)] - 100:
                cntr += 1

    return cntr


def solution2(grid: list[str]) -> int:
    track = get_track(grid)

    cntr = 0
    points = list(track.keys())
    for i in range(len(points) - 100):
        x0, y0 = points[i]
        for j in range(i + 100, len(points)):
            x1, y1 = points[j]
            cheats = abs(x1 - x0) + abs(y1 - y0)
            if cheats <= 20 and track[(x0, y0)] + cheats <= track[(x1, y1)] - 100:
                cntr += 1

    return cntr


grid = [line.rstrip() for line in stdin]
print(solution1(grid))
print(solution2(grid))
