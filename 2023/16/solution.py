from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)

# Linux only
def _solve(
        contraption: tuple[str],
        # beam start
        x: int = 0,
        y: int = 0,
        # beam direction
        dx: int = 1,
        dy: int = 0
    ) -> int:
    def beam(x: int, y: int, dx: int, dy: int):
        if x < 0 or x >= len(contraption[0]) or y < 0 or y >= len(contraption):
            return
        if (x, y, dx, dy) in energized:
            return

        energized.add((x, y, dx, dy))
        match contraption[y][x]:
            case '.':
                beam(x + dx, y + dy, dx, dy)
            case '-':
                if dy == 0:
                    beam(x + dx, y, dx, dy)
                else:
                    beam(x + 1, y, 1, 0)
                    beam(x - 1, y, -1, 0)
            case '|':
                if dx == 0:
                    beam(x, y + dy, dx, dy)
                else:
                    beam(x, y + 1, 0, 1)
                    beam(x, y - 1, 0, -1)
            case '/':
                beam(x - dy, y - dx, -dy, -dx)
            case '\\':
                beam(x + dy, y + dx, dy, dx)
            case _:
                raise ValueError

    energized = set()
    beam(x, y, dx, dy)
    energized = {(x, y) for x, y, *_ in energized}

    return len(energized)


def part1(contraption: tuple[str]) -> int:
    return _solve(contraption)


def part2(contraption: tuple[str]) -> int:
    energized = []
    max_x = len(contraption[0]) - 1
    max_y = len(contraption) -1

    for y in range(len(contraption)):
        energized.append(
            _solve(contraption, 0, y, 1, 0)
        )
        energized.append(
            _solve(contraption, max_x, y, -1, 0)
        )
    for x in range(len(contraption[0])):
        energized.append(
            _solve(contraption, x, 0, 0, 1)
        )
        energized.append(
            _solve(contraption, x, max_y, 0, -1)
        )

    return max(energized)


contraption = tuple(line.rstrip() for line in stdin)
print(part1(contraption))
print(part2(contraption))
