# https://adventofcode.com/2024/day/10
# # --- Day 10: Hoof It ---

from sys import stdin


def solution1(puzzle: list[list[int]]) -> int:
    def _dfs(x: int, y: int):
        visited.add((x, y))
        if puzzle[y][x] == 9:
            nonlocal ans
            ans += 1
            return
        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if (
                0 <= to_x < len(puzzle[0])
                and 0 <= to_y < len(puzzle)
                and (to_x, to_y) not in visited
                and puzzle[to_y][to_x] == puzzle[y][x] + 1
            ):
                _dfs(to_x, to_y)

    ans = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                visited = set()
                _dfs(j, i)

    return ans


def solution2(puzzle: list[list[int]]) -> int:
    def _dfs(x: int, y: int):
        if puzzle[y][x] == 9:
            nonlocal ans
            ans += 1
            return
        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if (
                0 <= to_x < len(puzzle[0])
                and 0 <= to_y < len(puzzle)
                and puzzle[to_y][to_x] == puzzle[y][x] + 1
            ):
                _dfs(to_x, to_y)

    ans = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                _dfs(j, i)

    return ans


puzzle = [list(map(int, line.rstrip())) for line in stdin]

print(solution1(puzzle))
print(solution2(puzzle))
