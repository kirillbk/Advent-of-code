from sys import stdin
from collections import deque


def part1(start: tuple[int, int], map: list[str]) -> int:
    q = deque()
    visited = {start: 0}

    q.append((start, 0))
    while q:
        cell, steps = q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1,0):
            x = cell[0] + dx
            y = cell[1] + dy
            if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
                continue
            if map[y][x] == '#':
                continue
            next_cell = (x, y)
            if next_cell not in visited:
                visited[next_cell] = steps + 1
                q.append((next_cell, steps + 1))

    answer = 0
    for _, steps in visited.items():
        if steps <= 64 and steps % 2 == 64 % 2:
            answer += 1

    return answer


def part2(start: tuple[int, int], map: list[str]) -> int:
    pass


def _get_start(map: list[str]) -> tuple[int, int]:
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                return x, y


map = stdin.read().splitlines()
start = _get_start(map)
print(part1(start, map))
print(part2(start, map))
