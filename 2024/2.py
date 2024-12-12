# https://adventofcode.com/2024/day/1
# --- Day 2: Red-Nosed Reports ---

from sys import stdin


def is_safe(r: list[int]) -> bool:
    is_asc = lambda x: all(x[i] < x[i + 1] for i in range(len(x) - 1))
    is_desc = lambda x: all(x[i] > x[i + 1] for i in range(len(x) - 1))

    if not (is_asc(r) or is_desc(r)):
        return False

    for i in range(len(r) - 1):
        diff = abs(r[i] - r[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


def solution1(reports: list[list[int]]) -> int:
    ans = 0
    for r in reports:
        if is_safe(r):
            ans += 1

    return ans


def solution2(reports: list[list[int]]) -> int:
    def _is_safe(r: list[int]) -> bool:
        if is_safe(r):
            return True

        for i in range(len(r)):
            tmp = r.pop(i)
            if is_safe(r):
                r.insert(i, tmp)
                return True
            r.insert(i, tmp)

        return False

    ans = 0
    for r in reports:
        if _is_safe(r):
            ans += 1

    return ans


reports = []
for line in stdin:
    r = map(int, line.split())
    r = list(r)
    reports.append(r)

print(solution1(reports))
print(solution2(reports))
