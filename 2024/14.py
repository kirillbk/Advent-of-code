# https://adventofcode.com/2024/day/14
# --- Day 14: Restroom Redoubt ---

from re import findall, search
from sys import stdin


def solution1(robots: list[tuple[int]]) -> int:
    q1 = q2 = q3 = q4 = 0
    for x, y, vx, vy in robots:
        px = (x + 100 * vx) % 101
        py = (y + 100 * vy) % 103
        if 0 <= px < 50:
            if 0 <= py < 51:
                q1 += 1
            elif 51 < py < 103:
                q2 += 1
        elif 50 < px < 101:
            if 0 <= py < 51:
                q3 += 1
            elif 51 < py < 103:
                q4 += 1

    return q1 * q2 * q3 * q4


def solution2(robots: list[tuple[int, int, int, int]]) -> int:
    for t in range(100000):
        grid = [[" "] * 101 for _ in range(103)]
        for x, y, vx, vy in robots:
            px = (x + t * vx) % 101
            py = (y + t * vy) % 103
            grid[py][px] = "@"

        for line in grid:
            s = "".join(line)
            if search(r"@{10}", s):
                print(*("".join(l) for l in grid), sep="\n")
                return t


robots = []
for line in stdin:
    x, y, vx, vy = map(int, findall(r"-?\d+", line))
    robots.append((x, y, vx, vy))

print(solution1(robots))
print(solution2(robots))
