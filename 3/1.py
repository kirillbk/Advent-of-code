from sys import stdin


def is_engine_part(schema: list[str], y: int, start: int, end: int) -> bool:
    dx = -1, 0, 1, -1, 1, -1, 0, 1
    dy = -1, -1, -1, 0, 0, 1, 1, 1

    for x in range(start, end):
        for i in range(8):
            symbol = schema[y + dy[i]][x + dx[i]]
            if not symbol.isdigit() and symbol != '.' and symbol != '\0':
                return True
    return False


schema = []
for line in stdin:
    schema.append('\0' + line.rstrip() + '\0')
schema.insert(0, '\0' * len(schema[0]))
schema.append('\0' * len(schema[0]))

answer = 0
for y in range(1, len(schema)):
    start = None
    for x in range(1, len(schema[0])):
        if not start and schema[y][x].isdigit():
            start = x
        elif start and not schema[y][x].isdigit():
            if is_engine_part(schema, y, start, x):
                answer += int(schema[y][start:x])
            start = None

print(answer)
