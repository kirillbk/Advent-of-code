# https://adventofcode.com/2024/day/21
# --- Day 21: Keypad Conundrum ---

from functools import cache
from sys import stdin


NUMPAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    " ": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}


def solution(codes: list[str], n: int) -> int:
    @cache
    def _shortest_length(
        x0: int, y0: int, x1: int, y1: int, robot: int, gap: tuple[int, int] = (0, 0)
    ) -> int:
        if robot == 0:
            return 0

        dx = x1 - x0
        dy = y1 - y0
        length = abs(dx) + abs(dy)

        x_then_y = y_then_x = float("inf")
        x_move = (2, 1) if dx > 0 else (0, 1) if dx < 0 else (2, 0)
        y_move = (1, 1) if dy > 0 else (1, 0) if dy < 0 else (2, 0)

        if (x1, y0) != gap:
            x_then_y = (
                _shortest_length(2, 0, *x_move, robot - 1)
                + _shortest_length(*x_move, *y_move, robot - 1)
                + _shortest_length(*y_move, 2, 0, robot - 1)
            )
        if (x0, y1) != gap:
            y_then_x = (
                _shortest_length(2, 0, *y_move, robot - 1)
                + _shortest_length(*y_move, *x_move, robot - 1)
                + _shortest_length(*x_move, 2, 0, robot - 1)
            )

        return length + min(x_then_y, y_then_x)

    def _code_length(code: str) -> int:
        cntr = len(code)
        y, x = NUMPAD["A"]
        for button in code:
            to_y, to_x = NUMPAD[button]
            cntr += _shortest_length(x, y, to_x, to_y, n, (0, 3))
            x, y = to_x, to_y

        return cntr

    ans = 0
    for code in codes:
        ans += _code_length(code) * int(code[:-1])

    return ans


codes = stdin.read().split()

print(solution(codes, 3))
print(solution(codes, 26))
