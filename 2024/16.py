# https://adventofcode.com/2024/day/16
# --- Day 16: Reindeer Maze ---

from collections import defaultdict
from functools import partial
from heapq import heappush, heappop
from sys import stdin


STEPS = (0, 1), (0, -1), (1, 0), (-1, 0)


def find_tile(grid: list[str], tile: str) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == tile:
                return j, i
    return -1, -1


def dijkstra(
    x_start: int, y_start: int, x_end: int, y_end: int, grid: list[str]
) -> defaultdict[tuple[int, int, int, int], int | float]:
    dist = defaultdict(partial(float, "inf"))
    dist[(x_start, y_start, 1, 0)] = 0
    q = [
        (0, (x_start, y_start, 1, 0)),
    ]
    while q:
        d, tile = heappop(q)
        if d != dist[tile]:
            continue

        x, y, dx, dy = tile
        if x == x_end and y == y_end:
            continue

        steps = (dx, dy, d + 1), (-dy, dx, d + 1001), (dy, -dx, d + 1001)
        for dx, dy, to_d in steps:
            to_x = x + dx
            to_y = y + dy
            to_tile = (to_x, to_y, dx, dy)
            if grid[to_y][to_x] != "#" and to_d <= dist[to_tile]:
                dist[to_tile] = to_d
                heappush(q, (to_d, to_tile))

    return dist


def solution1(grid: list[str]) -> int:
    x_start, y_start = find_tile(grid, "S")
    x_end, y_end = find_tile(grid, "E")
    dist = dijkstra(x_start, y_start, x_end, y_end, grid)

    return min(dist[(x_end, y_end, dx, dy)] for dx, dy in STEPS)


def solution2(grid: list[str]) -> int:
    def _dfs(x: int, y: int, prev_d: int):
        if (x, y) in visited:
            return
        visited.add((x, y))
        if x == x_start and y == y_start:
            return

        for dx, dy in STEPS:
            d = dist[(x, y, dx, dy)]
            if d == prev_d - 1 or d == prev_d - 1001:
                _dfs(x - dx, y - dy, d)

    x_start, y_start = find_tile(grid, "S")
    x_end, y_end = find_tile(grid, "E")
    dist = dijkstra(x_start, y_start, x_end, y_end, grid)
    score = min(dist[(x_end, y_end, dx, dy)] for dx, dy in STEPS)

    visited = set()
    _dfs(x_end, y_end, score + 1)

    return len(visited)


grid = stdin.read().split()

print(solution1(grid))
print(solution2(grid))
