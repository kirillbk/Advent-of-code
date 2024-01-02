from sys import stdin, setrecursionlimit


def part1(start: tuple[int, int], finish: tuple[int, int], grid: set[str]) -> int:
    def dfs(cell: tuple[int, int], visited: list[tuple[int, int]]):
        if cell in visited:
            return
        if cell == finish:
            nonlocal answer
            answer = max(len(visited), answer)
            return

        visited.add(cell)

        for dx, dy in (0, 1), ( 0, -1), (1, 0), (-1, 0):
            x = cell[0] + dx
            y = cell[1] + dy
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                continue
            if grid[y][x] == '#':
                continue
            elif grid[y][x] == '<' and (dx != -1 or dy != 0):
                continue
            elif grid[y][x] == '>' and (dx != 1 or dy != 0):
                continue
            elif grid[y][x] == '^' and (dx != 0 or dy != -1):
                continue
            elif grid[y][x] == 'v' and (dx != 0 or dy != 1):
                continue
            dfs((x, y), visited)

        visited.remove(cell)

    answer = -1
    visited = set()
    # visited.add(start)
    setrecursionlimit(10**6)
    dfs(start, visited)
    # for y in range(len(grid)):
    #     for x in range(len(grid)):
    #         c = 'O' if (x, y) in visited else grid[y][x]
    #         print(c, end='')
    #     print()

    return answer


grid = stdin.read().splitlines()
start = (grid[0].index('.'), 0)
finish = (grid[-1].index('.'), len(grid) - 1)

print(part1(start, finish, grid))
