# https://adventofcode.com/2024/day/7
# --- Day 7: Bridge Repair ---

from collections.abc import Callable, Iterable
from operator import add, mul
from sys import stdin


def check_equation(
    val: int,
    nums: list[int],
    operators: Iterable[Callable[[int, int], int]],
    res: int,
    i: int,
) -> bool:
    if res > val:
        return False
    if i == len(nums):
        return val == res
    for op in operators:
        if check_equation(val, nums, operators, op(res, nums[i]), i + 1):
            return True
    return False


def solution1(equations: list[tuple[int, list[int]]]) -> int:
    operators = add, mul
    ans = 0
    for val, nums in equations:
        if check_equation(val, nums, operators, nums[0], 1):
            ans += val

    return ans


def solution2(equations: list[tuple[int, list[int]]]) -> int:
    operators = add, mul, lambda x, y: int(f"{x}{y}")
    ans = 0
    for val, nums in equations:
        if check_equation(val, nums, operators, nums[0], 1):
            ans += val

    return ans


equations = []
for line in stdin:
    val, nums = line.split(":")
    val = int(val)
    nums = list(map(int, nums.split()))
    equations.append((val, nums))


print(solution1(equations))
print(solution2(equations))
