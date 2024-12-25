# https://adventofcode.com/2024/day/25
# --- Day 25: Code Chronicle ---

from sys import stdin


def solution1(keys_and_locks: list[list[str]]) -> int:
    keys = []
    locks = []
    for item in keys_and_locks:
        tmp = ("".join(line) for line in zip(*item))
        heigts = tuple(line.count("#") - 1 for line in tmp)
        if item[0].startswith("#"):
            locks.append(heigts)
        else:
            keys.append(heigts)

    ans = 0
    for key in keys:
        for lock in locks:
            if all(sum(x) <= 5 for x in zip(key, lock)):
                ans += 1

    return ans


puzzle = [item.split() for item in stdin.read().split("\n\n")]
print(solution1(puzzle))
