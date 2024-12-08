# --- Day 8: Resonant Collinearity ---

from collections import defaultdict
from sys import stdin


def solution1(antennas: defaultdict[str, tuple[int, int]]) -> int:
    is_in_map = lambda x, y: 0 <= x < len(puzzle[0]) and 0 <= y < len(puzzle)
    antinodes = set()
    for group in antennas.values():
        for i in range(len(group) - 1):
            x0, y0 = group[i]
            for j in range(i + 1, len(group)):
                x1, y1 = group[j]
                dx = x1 - x0
                dy = y1 - y0

                ax = x0 - dx
                ay = y0 - dy
                if is_in_map(ax, ay):
                    antinodes.add((ax, ay))
                ax = x1 + dx
                ay = y1 + dy
                if is_in_map(ax, ay):
                    antinodes.add((ax, ay))

    return len(antinodes)


def solution2(antennas: defaultdict[str, tuple[int, int]]) -> int:
    def _add_antinodes(x, y, dx, dy, antinodes: set[tuple[int, int]]):
        while 0 <= x < len(puzzle[0]) and 0 <= y < len(puzzle):
            antinodes.add((x, y))
            x += dx
            y += dy

    antinodes = set()
    for group in antennas.values():
        for i in range(len(group) - 1):
            x0, y0 = group[i]
            for j in range(i + 1, len(group)):
                x1, y1 = group[j]
                dx = x1 - x0
                dy = y1 - y0
                _add_antinodes(x0, y0, -dx, -dy, antinodes)
                _add_antinodes(x1, y1, dx, dy, antinodes)

    return len(antinodes)


puzzle = [line[:-1] for line in stdin]

antennas = defaultdict(list)
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j].isalnum():
            antennas[puzzle[i][j]].append((j, i))

print(solution1(antennas))
print(solution2(antennas))
