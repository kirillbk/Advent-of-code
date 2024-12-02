from collections import Counter
from sys import stdin


def solution1(a: list[int], b: list[int]) -> int:
    a = sorted(a)
    b = sorted(b)
    tmp = (abs(a_ - b_) for a_, b_ in zip(a, b))

    return sum(tmp)


def solution2(a: list[int], b: list[int]) -> int:
    cntr = Counter(b)
    tmp = (a_ * cntr[a_] for a_ in a)

    return sum(tmp)


a, b = [], []
for line in stdin:
    a_, b_ = map(int, line.split())
    a.append(a_)
    b.append(b_)

print(solution1(a, b))
print(solution2(a, b))
