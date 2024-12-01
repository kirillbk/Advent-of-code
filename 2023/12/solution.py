from sys import stdin
from functools import cache


class Solution:
    def __init__(self) -> None:
        self._conditions = []
        for line in stdin:
            springs, groups = line.split()
            groups = groups.split(',')
            groups = tuple(map(int, groups))
            self._conditions.append((springs, groups))

    @staticmethod
    @cache
    def _solve(springs: str, groups: tuple[int]) -> int:
        # skip '.' - no new variants
        springs = springs.lstrip('.')

        if not groups:
            return 1 if '#' not in springs else 0
        if not springs:
            return 0

        arrangements = 0
        # branch '?' -> '.'
        if springs[0] == '?':
            arrangements += Solution._solve(springs[1:], groups)
        # branch '#' or '?' -> '#'
        group_size = groups[0]
        # next group_size symbols -> '#' and [group_size + 1] != '#'
        if (
            group_size <= len(springs)
            and springs.find('.', 0, group_size) == -1
            and (group_size == len(springs) or springs[group_size] != '#')
        ):
            arrangements += Solution._solve(springs[group_size + 1:], groups[1:])

        return arrangements

    def solve1(self) -> int:
        answer = 0
        for springs, groups in self._conditions:
            answer +=self._solve(springs, groups)

        return answer

    def solve2(self) -> int:
        answer = 0
        for springs, groups in self._conditions:
            answer +=self._solve('?'.join((springs,) * 5), groups * 5)

        return answer


solution = Solution()
print(solution.solve1())
print(solution.solve2())
