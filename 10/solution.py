from sys import stdin
from collections import deque


class Solution:

    def __init__(self) -> None:
        self._pipes = stdin.read().splitlines()

        for y in range(len(self._pipes)):
            for x in range(len(self._pipes[0])):
                if self._pipes[y][x] == 'S':
                    self._x_start = x
                    self._y_start = y
                    return

    def _get_loop(self) -> dict[tuple[int, int], int]:
        steps = {
            'S': ((0, -1), (0, 1), (-1, 0), (1, 0)),
            '|': ((0, 1), (0, -1)),
            '-': ((1, 0), (-1, 0)),
            'L': ((0, -1), (1, 0)),
            'J': ((-1, 0), (0, -1)),
            '7': ((-1, 0), (0, 1)),
            'F': ((1, 0), (0, 1)),
            '.': ()
        }
        loop: dict[tuple[int, int], int] = {}
        q: deque[int, int, int] = deque()

        q.append((self._y_start, self._x_start, 0))
        loop[(self._y_start, self._x_start)] = 0
        while q:
            y, x, d = q.popleft()
            pipe = self._pipes[y][x]
            for dx, dy in steps[pipe]:
                x_ = x + dx
                y_ = y + dy
                if x_ < 0 or y_ < 0 or x_ >= len(self._pipes[0]) or y_ >= len(self._pipes):
                    continue
                next_pipe = self._pipes[y_][x_]
                if (y_, x_) not in loop and (-dx, -dy) in steps[next_pipe]:
                    loop[(y_, x_)] = d + 1
                    q.append((y_, x_, d + 1))

        return loop

    def solve1(self) -> int:
        loop = self._get_loop()

        return max(loop.values())

    def _is_inside_loop(self, y: int, x: int, loop: set[tuple[int, int]]) -> int:
        hits = 0
        first_pipe = '\0'

        for x in range(x + 1, len(self._pipes[0])):
            if (y, x) not in loop:
                continue
            pipe = self._pipes[y][x]
            if (
                pipe == '|'
                or pipe == '7' and first_pipe == 'L'
                or pipe == 'J' and first_pipe == 'F'
            ):
                hits += 1
            elif pipe in 'LF':
                first_pipe = pipe

        return hits % 2 != 0

    def _replace_start_to_pipe(self, loop: set[tuple[int, int]]):
        pipes = self._pipes
        y, x = self._y_start, self._x_start
        top = down = left = right = False

        if (y - 1, x) in loop and pipes[y - 1][x] in '|F7':
            top = True
        if (y + 1, x) in loop and pipes[y + 1][x] in '|LJ':
            down = True
        if (y, x - 1) in loop and pipes[y][x - 1] in '-FL':
            left = True
        if (y, x + 1) in loop and pipes[y][x + 1] in '-J7':
            right = True

        if left and right:
            pipe = '-'
        elif top and down:
            pipe = '|'
        elif top and left:
            pipe = 'J'
        elif top and right:
            pipe = 'L'
        elif left and down:
            pipe = '7'
        elif right and down:
            pipe = 'F'

        pipes[y] = pipes[y].replace('S', pipe)


    def solve2(self) -> int:
        loop = self._get_loop().keys()
        answer = 0

        self._replace_start_to_pipe(loop)

        for y in range(len(self._pipes)):
            for x in range(len(self._pipes[0])):
                if (y, x) not in loop and self._is_inside_loop(y, x, loop):
                    answer += 1

        return answer


solution = Solution()
print(solution.solve1())
print(solution.solve2())
