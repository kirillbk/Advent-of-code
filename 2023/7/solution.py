from sys import stdin
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self._hands = []

        for line in stdin:
            hand, bid = line.split()
            self._hands.append((hand, int(bid)))

    @staticmethod
    def _get_rank(hand: list[str], joker: bool = False) -> int:
        first_max = second_max = jokers = 0
        for card, n in Counter(hand).items():
            if joker and card == 'J':
                jokers = n
                continue
            if n > first_max:
                second_max = first_max
                first_max = n
            elif n > second_max:
                second_max = n
        first_max = first_max + jokers

        if first_max == 5:
           return 6
        elif first_max == 4:
           return 5
        elif first_max == 3 and second_max == 2:
           return 4
        elif first_max == 3:
           return 3
        elif first_max == second_max == 2:
           return 2
        elif first_max == 2:
           return 1
        return 0

    def solve1(self) -> int:
        table = str.maketrans('TJQKA', 'ABCDE')
        key_function = lambda x: (self._get_rank(x[0]), x[0].translate(table))
        hands = sorted(self._hands, key=key_function)

        answer = 0
        for i, hand in enumerate(hands, 1):
            answer += hand[1] * i

        return answer

    def solve2(self) -> int:
        table = str.maketrans('TJQKA', 'A1BCD')
        key_function = lambda x: (self._get_rank(x[0], True), x[0].translate(table))
        hands = sorted(self._hands, key=key_function)

        answer = 0
        for i, hand in enumerate(hands, 1):
            answer += hand[1] * i

        return answer

solution = Solution()
print(solution.solve1())
print(solution.solve2())

