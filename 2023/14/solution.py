from sys import stdin
from copy import deepcopy


def part1(platform: list[str]) -> int:
    answer = 0
    for x in range(len(platform[0])):
        i = None
        for y in range(len(platform)):
            match platform[y][x]:
                case '.':
                    if i is None:
                        i = y
                case '#':
                    i = None
                case 'O':
                    if i is None:
                        answer += len(platform) - y
                    else:
                        answer += len(platform) - i
                        i += 1

    return answer


def _tilt_north(platform: list[str]):
    for x in range(len(platform[0])):
        i = None
        for y in range(len(platform)):
            tile = platform[y][x]
            if tile == '.' and i is None:
                i = y
            elif tile == '#':
                i = None
            elif tile == 'O' and i is not None:
                platform[i][x], platform[y][x] = 'O', '.'
                i += 1


def part2(platform: list[str]) -> int:
    N = 10**9
    states = [deepcopy(platform)]

    for i in range(N):
        # north, west, south, east
        for _ in range(4):
            _tilt_north(platform)
            # rotate clockwise
            platform = list(list(line) for line in zip(*reversed(platform)))

        # platform state duplicated
        try:
            j = states.index(platform)
            k = (N - j) % (i - j + 1)
            # N-th state
            platform = states[j + k]
            break
        except ValueError:
            states.append(deepcopy(platform))

    answer = 0
    for x in range(len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] == 'O':
                answer += len(platform) - y

    return answer


platform = [list(line.rstrip()) for line in stdin]
print(part1(platform))
print(part2(platform))
