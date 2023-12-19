from sys import stdin


def _get_points(dig_plan: tuple[tuple[str, int, str]]) -> list[tuple[int, int]]:
    dir = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    points = [(0, 0)]

    for d, l, *_ in dig_plan:
        dx, dy = dir[d]
        x, y  = points[-1]
        next_point = x + dx * l, y + dy * l
        points.append(next_point)

    return points


def _get_area(points: tuple[tuple[int, int]]) -> int:
    # shoelace formula
    sum = 0
    for i in range(len(points) - 1):
        sum += points[i][0] * points[i + 1][1]
        sum -= points[i + 1][0] * points[i][1]

    return abs(sum) // 2


def part1(dig_plan: tuple[tuple[str, int, str]]) -> int:
    points = _get_points(dig_plan)
    area = _get_area(points)
    p = sum(item[1] for item in dig_plan)

    # according Pick's theorem
    return area + p // 2 + 1


def part2(dig_plan: tuple[tuple[str, int, str]]) -> int:
    plan = []
    dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    for _, _, color in dig_plan:
        color = color.strip('()#')
        d = dir[color[-1]]
        l = int(color[:-1], 16)
        plan.append((d, l))

    return (part1(plan))


dig_plan = []
for line in stdin:
    d, l, c = line.split()
    l = int(l)
    dig_plan.append((d, l, c))

print(part1(dig_plan))
print(part2(dig_plan))
