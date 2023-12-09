from sys import stdin


class Solution:
    def __init__(self) -> None:
        self._history = []
        for line in stdin:
            values = map(int, line.split())
            values = list(values)
            self._history.append(values)

    @staticmethod
    def _get_next_value(seq: list[int]) -> int:
        if all(n == 0 for n in seq):
            return 0
        next_seq = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        a = Solution._get_next_value(next_seq)

        return seq[-1] + a

    def solve1(self) -> int:
        next_values = (self._get_next_value(seq) for seq in self._history)

        return sum(next_values)

    def solve2(self) -> int:
        prev_values  = (self._get_next_value(seq[::-1]) for seq in self._history)

        return sum(prev_values)


solution = Solution()
print(solution.solve1())
print(solution.solve2())
