# https://adventofcode.com/2024/day/19
# --- Day 19: Linen Layout ---

from functools import cache
from sys import stdin


@cache
def make_towel(towel: str, patterns: tuple[str]) -> int:
    if not towel:
        return 1

    variants = 0
    for p in patterns:
        if towel.startswith(p):
            variants += make_towel(towel[len(p) :], patterns)

    return variants


def solution1(patterns: list[str], towels: list[str]) -> int:
    ans = 0
    for t in towels:
        if make_towel(t, patterns):
            ans += 1

    return ans


def solution2(patterns: list[str], towels: tuple[str]) -> int:
    return sum(make_towel(t, patterns) for t in towels)


patterns = tuple(input().split(", "))
input()
towels = [line.rstrip() for line in stdin]

print(solution1(patterns, towels))
print(solution2(patterns, towels))
