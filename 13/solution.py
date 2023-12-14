from sys import stdin
from typing import Callable, TextIO


class Solution:
    def __init__(self, file: TextIO) -> None:
        self._patterns = [pattern.split() for pattern in file.read().split('\n\n')]

    def _solve(self, reflection_func: Callable[[str], int]) -> int:
        answer = 0
        for pattern in self._patterns:
            answer += reflection_func(pattern) * 100 + reflection_func(list(zip(*pattern)))

        return answer

    def solve1(self) -> int:
        def get_reflection(pattern: list[str]) -> int:
            for i in range(1, len(pattern)):
                n = min(len(pattern) - i, i)
                if pattern[i - n:i] == pattern[i + n - 1: i - 1: -1]:
                    return i
            return 0

        return self._solve(get_reflection)

    def solve2(self) -> int:
        def get_reflection(pattern: list[str]) -> int:
            for i in range(1, len(pattern)):
                difff = 0
                for j in range(min(len(pattern) - i, i)):
                    line1 = pattern[i + j]
                    line2 = pattern[i - j - 1]
                    difff += sum(1 for a, b in zip(line1, line2) if a != b)
                if difff == 1:
                    return i
            return 0

        return self._solve(get_reflection)


solution = Solution(stdin)
print(solution.solve1())
print(solution.solve2())
