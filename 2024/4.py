# https://adventofcode.com/2024/day/4
# --- Day 4: Ceres Search ---

from sys import stdin


def solution1(puzzle: list[list[str]]) -> int:
    def _is_pattern(x: int, y: int, dx: int, dy: int) -> bool:
        s = ""
        while len(s) < len(pattern):
            if x < 0 or x >= len(puzzle[0]) or y < 0 or y >= len(puzzle):
                return False
            s += puzzle[y][x]
            x += dx
            y += dy

        return s == pattern

    total = 0
    pattern = "XMAS"
    steps = (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if pattern.startswith(puzzle[i][j]):
                for dx, dy in steps:
                    if _is_pattern(j, i, dx, dy):
                        total += 1

    return total


def solution2(puzzle: list[list[str]]) -> int:
    def _is_xmas(x: int, y: int) -> bool:
        if puzzle[y][x] != "A":
            return False

        l, r = x - 1, x + 1
        t, d = y - 1, y + 1
        if t < 0 or d >= len(puzzle) or l < 0 or r >= len(puzzle[0]):
            return False

        tl, tr = puzzle[t][l], puzzle[t][r]
        bl, br = puzzle[d][l], puzzle[d][r]
        if (tl == "M" and br == "S" or tl == "S" and br == "M") and (
            tr == "M" and bl == "S" or tr == "S" and bl == "M"
        ):
            return True
        return False

    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if _is_xmas(j, i):
                total += 1

    return total


puzzle = stdin.readlines()

print(solution1(puzzle))
print(solution2(puzzle))
