# https://adventofcode.com/2024/day/12
# --- Day 12: Garden Groups ---

from sys import stdin


def solution1(farm: list[str]) -> int:
    def _dfs(x: int, y: int, kind: str):
        nonlocal area, perimeter
        visited[y][x] = True
        area += 1
        perimeter += 4
        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if (
                0 <= to_x < len(farm[0])
                and 0 <= to_y < len(farm)
                and farm[to_y][to_x] == kind
            ):
                perimeter -= 1
                if not visited[to_y][to_x]:
                    _dfs(to_x, to_y, kind)

    visited = [[False] * len(puzzle[0]) for _ in range(len(farm))]
    ans = 0
    for i in range(len(farm)):
        for j in range(len(farm)):
            if not visited[i][j]:
                area = perimeter = 0
                _dfs(j, i, farm[i][j])
                ans += area * perimeter

    return ans


def solution2(farm: list[str]) -> int:
    is_inside = lambda x, y: 0 <= x < len(puzzle[0]) and 0 <= y < len(puzzle)

    def _find_corners(x: int, y: int, kind: str):
        nonlocal sides
        dx, dy = 1, 0
        ddx, ddy = 1, 1
        for _ in range(4):
            x1, y1 = x + dx, y + dy
            x2, y2 = x - dy, y + dx
            if (not is_inside(x1, y1) or farm[y1][x1] != kind) and (
                not is_inside(x2, y2) or farm[y2][x2] != kind
            ):
                sides += 1
            elif (
                is_inside(x1, y1)
                and farm[y1][x1] == kind
                and is_inside(x2, y2)
                and farm[y2][x2] == kind
                and farm[y + ddy][x + ddx] != kind
            ):
                sides += 1

            dx, dy = -dy, dx
            ddx, ddy = -ddy, ddx

    def _dfs(x: int, y: int, kind: str):
        nonlocal area
        visited[y][x] = True
        area += 1
        _find_corners(x, y, kind)
        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if (
                is_inside(to_x, to_y)
                and not visited[to_y][to_x]
                and farm[to_y][to_x] == kind
            ):
                _dfs(to_x, to_y, kind)

    visited = [[False] * len(puzzle[0]) for _ in range(len(farm))]
    ans = 0
    for i in range(len(farm)):
        for j in range(len(farm)):
            if not visited[i][j]:
                area = sides = 0
                _dfs(j, i, farm[i][j])
                ans += area * sides

    return ans


puzzle = [line.rstrip() for line in stdin]

print(solution1(puzzle))
print(solution2(puzzle))
