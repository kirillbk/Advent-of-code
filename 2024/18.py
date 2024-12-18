# --- Day 18: RAM Run ---
# https://adventofcode.com/2024/day/17

from collections import deque
from sys import stdin


def bfs(
    x_start: int, y_start: int, x_end: int, y_end: int, bytes: set[tuple[int, int]]
) -> int:
    visited = set()
    q = deque()
    visited.add((x_start, y_start))
    q.append((0, x_start, y_start))
    while q:
        d, x, y = q.popleft()
        if x == x_end and y == y_end:
            return d

        steps = (0, 1), (0, -1), (1, 0), (-1, 0)
        for dx, dy in steps:
            to_x = x + dx
            to_y = y + dy
            if (
                0 <= to_x < 71
                and 0 <= to_y < 71
                and (to_x, to_y) not in visited
                and (to_x, to_y) not in bytes
            ):
                visited.add((to_x, to_y))
                q.append((d + 1, to_x, to_y))

    return -1


def solution1(bytes: list[tuple[int, int]]) -> int:
    bytes = set(bytes[i] for i in range(1024))

    return bfs(0, 0, 70, 70, bytes)


def solution2(bytes: list[tuple[int, int]]) -> str | None:
    fallen_bytes = set(bytes[i] for i in range(1024))
    for i in range(1024, len(bytes)):
        x, y = bytes[i]
        fallen_bytes.add((x, y))
        if bfs(0, 0, 70, 70, fallen_bytes) == -1:
            return f"{x},{y}"

    return None


bytes = []
for line in stdin:
    x, y = map(int, line.split(","))
    bytes.append((x, y))

print(solution1(bytes))
print(solution2(bytes))
