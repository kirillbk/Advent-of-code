# --- Day 7: Bridge Repair ---

from sys import stdin


def solution1(puzzle: list[tuple[int, list[int]]]) -> int:
    def _check_equation(res: int, i: int) -> bool:
        if res > val:
            return False
        if i == len(nums):
            return val == res
        return _check_equation(res * nums[i], i + 1) or _check_equation(
            res + nums[i], i + 1
        )

    ans = 0
    for val, nums in puzzle:
        if _check_equation(nums[0], 1):
            ans += val

    return ans


def solution2(puzzle: list[tuple[int, list[int]]]) -> int:
    def _check_equation(res: int, i: int) -> bool:
        if res > val:
            return False
        if i == len(nums):
            return val == res
        return (
            _check_equation(res * nums[i], i + 1)
            or _check_equation(res + nums[i], i + 1)
            or _check_equation(int(f"{res}{nums[i]}"), i + 1)
        )

    ans = 0
    for val, nums in puzzle:
        if _check_equation(nums[0], 1):
            ans += val

    return ans


puzzle = []
for line in stdin:
    val, nums = line.split(":")
    val = int(val)
    nums = list(map(int, nums.split()))
    puzzle.append((val, nums))


print(solution1(puzzle))
print(solution2(puzzle))
