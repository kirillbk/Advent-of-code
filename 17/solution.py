from sys import stdin
from heapq import heappush, heappop


def _solve(
        start: tuple[int, int],
        finish: tuple[int, int],
        grid: tuple[tuple[int]],
        max_steps: int = 3,
        min_steps: int = 1
    ) -> int:

    visited = set()
    # distance, (x, y), (dx, dy), steps in current direction
    q = [(0, start, (1, 0), 1), (0, start, (0, 1), 1)]

    while q:
        d, cell, dir, steps = heappop(q)

        state = cell, dir, steps
        if state in visited:
            continue
        visited.add(state)

        # move a minimum of "min_steps" blocks in that direction before it can stopped
        if cell == finish and steps >= min_steps:
            return d

        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_cell = cell[0] + dx, cell[1] + dy
            next_dir = dx, dy
            next_steps = steps + 1 if dir == next_dir else 1

            # out of grid
            if next_cell[0] < 0 or next_cell[0] >= len(grid[0]) or next_cell[1] < 0 or next_cell[1] >= len(grid):
                continue
            # reverse direction
            if -dir[0] == dx and -dir[1] == dy:
                continue
            # move more than "max_steps" blocks in a single direction
            if next_steps > max_steps:
                continue
            # move a minimum of "min_steps" blocks in that direction before it can turn
            if dir != next_dir and steps < min_steps:
                continue

            next_d = d + grid[next_cell[1]][next_cell[0]]
            heappush(
                q,
                (next_d, next_cell, next_dir, next_steps),
            )


def part1(start: tuple[int, int], finish: tuple[int, int], grid: tuple[tuple[int]]) -> int:

    return _solve(start, finish, grid)


def part2(start: tuple[int, int], finish: tuple[int, int], grid: tuple[tuple[int]]) -> int:

    return _solve(start, finish, grid, 10, 4)


grid = (line.rstrip() for line in stdin)
grid = (map(int, line) for line in grid)
grid = tuple(map(tuple, grid))
start = 0, 0
finish = len(grid[0]) - 1, len(grid) - 1

print(part1(start, finish, grid))
print(part2(start, finish, grid))
