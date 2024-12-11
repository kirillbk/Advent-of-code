# --- Day 11: Plutonian Pebbles ---

from functools import cache


def solution1(stones: list[int]) -> int:
    next_stones = []
    for _ in range(25):
        for i in range(len(stones)):
            if stones[i] == 0:
                next_stones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                s = str(stones[i])
                s1 = int(s[: len(s) // 2])
                s2 = int(s[len(s) // 2 :])
                next_stones.append(s1)
                next_stones.append(s2)
            else:
                next_stones.append(stones[i] * 2024)
        stones = next_stones
        next_stones = []

    return len(stones)


def solution2(stones: list[int]) -> int:
    @cache
    def _count(stone: int, n: int) -> int:
        for i in range(n):
            if stone == 0:
                stone = 1
                continue
            s = str(stone)
            if len(s) % 2:
                stone *= 2024
            else:
                stone1 = int(s[: len(s) // 2])
                stone2 = int(s[len(s) // 2 :])
                return _count(stone1, n - i - 1) + _count(stone2, n - i - 1)

        return 1

    return sum(_count(stone, 75) for stone in stones)


stones = list(map(int, input().split()))

print(solution1(stones))
print(solution2(stones))
