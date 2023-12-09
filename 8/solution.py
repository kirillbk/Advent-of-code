from sys import stdin
from itertools import cycle
from math import lcm
from typing import Callable


class Solution:
    def __init__(self) -> None:
        self._instructions = stdin.readline().rstrip()
        self._nodes = {}
        stdin.readline()
        for line in stdin:
            node = line[:3]
            left = line[7:10]
            right = line[12:15]
            self._nodes[node] = left, right

    def solve1(self,
               node: str = 'AAA',
               is_finish: Callable[[str], bool] = lambda x: x == 'ZZZ'
               ) -> int:
        steps = 0

        for dir in cycle(self._instructions):
            if is_finish(node):
                break
            steps += 1
            match dir:
                case 'L':
                    node = self._nodes[node][0]
                case 'R':
                    node = self._nodes[node][1]

        return steps

    def solve2(self) -> int:
        nodes = [node for node in self._nodes if node.endswith('A')]
        is_finish = lambda x: x.endswith('Z')
        steps = (self.solve1(node, is_finish) for node in nodes)

        return lcm(*steps)


solution = Solution()
print(solution.solve1())
print(solution.solve2())
