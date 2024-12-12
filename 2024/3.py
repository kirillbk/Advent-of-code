# https://adventofcode.com/2024/day/3
# --- Day 3: Mull It Over ---

from re import findall, X
from sys import stdin


def solution1(s: str) -> int:
    total = 0
    for m in findall(r"mul\((\d+),(\d+)\)", s):
        a, b = map(int, m)
        total += a * b

    return total


def solution2(s: str) -> int:
    total = 0
    enable = True
    pattern = r"""
        (do)\( \)
        | (don't)\( \)
        | mul\( (\d+),(\d+) \)
    """
    for m in findall(pattern, s, X):
        if m[0]:
            enable = True
        elif m[1]:
            enable = False
        elif enable:
            total += int(m[2]) * int(m[3])

    return total


s = stdin.read()

print(solution1(s))
print(solution2(s))
