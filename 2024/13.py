# https://adventofcode.com/2024/day/13
# --- Day 13: Claw Contraption ---

from math import isinf
from re import findall
from sys import stdin


def solution1(machines: list[tuple[int]]) -> int:
    ans = 0
    for ax, ay, bx, by, px, py in machines:
        cost = float("inf")
        for i in range(1, 101):
            nx, rx = divmod(px - i * ax, bx)
            ny, ry = divmod(py - i * ay, by)
            if nx == ny and rx == ry == 0:
                cost = min(cost, i * 3 + nx)
        if not isinf(cost):
            ans += cost

    return ans


def solution2(machines: list[tuple[int]]) -> int:
    def _solve_equation(
        ax: int, ay: int, bx: int, by: int, px: int, py: int
    ) -> tuple[int, int]:
        px += 10000000000000
        py += 10000000000000
        det = ax * by - ay * bx
        na = (px * by - py * bx) // det
        nb = (ax * py - ay * px) // det
        if na * ax + nb * bx == px and na * ay + nb * by == py:
            return na, nb
        return 0, 0

    ans = 0
    for m in machines:
        nx, ny = _solve_equation(*m)
        ans += nx * 3 + ny

    return ans


puzzle = []
for m in stdin.read().split("\n\n"):
    ax, ay, bx, by, px, py = list(map(int, findall(r"\d+", m)))
    puzzle.append((ax, ay, bx, by, px, py))

print(solution1(puzzle))
print(solution2(puzzle))
