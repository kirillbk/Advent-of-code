# https://adventofcode.com/2024/day/5
# --- Day 5: Print Queue ---

from collections import defaultdict
from sys import stdin


def solution1(rules: defaultdict[set[int]], updates: list[list[int]]) -> int:
    def _is_update_ok(update: list[int]) -> bool:
        printed = set()
        for p in update:
            if not printed.isdisjoint(rules[p]):
                return False
            printed.add(p)

        return True

    ans = 0
    for u in updates:
        if _is_update_ok(u):
            ans += u[len(u) // 2]

    return ans


def solution2(rules: defaultdict[set[int]], updates: list[list[int]]) -> int:
    def _print_update(update: list[int]) -> list[int]:
        printed = []
        for p in update:
            for i in range(len(printed)):
                if printed[i] in rules[p]:
                    printed.insert(i, p)
                    break
            else:
                printed.append(p)

        return printed

    ans = 0
    for u in updates:
        pages = _print_update(u)
        if pages != u:
            ans += pages[len(pages) // 2]

    return ans


tmp, updates = stdin.read().split("\n\n")

updates = (u.split(",") for u in updates.split())
updates = [list(map(int, u)) for u in updates]

tmp = (r.split("|") for r in tmp.split())
rules = defaultdict(set)
for r in tmp:
    a, b = map(int, r)
    rules[a].add(b)

print(solution1(rules, updates))
print(solution2(rules, updates))
