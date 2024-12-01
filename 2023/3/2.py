from sys import stdin


def get_parts(schema: list[str], y: int, x: int) -> list[int]:
    parts = []
    dx = -1, 0, 1, -1, 1, -1, 0, 1
    dy = -1, -1, -1, 0, 0, 1, 1, 1

    for i in range(8):
        x_ = x + dx[i]
        y_ = y + dy[i]

        if x_ < 0 or x_ >= len(schema[0]) or y_ < 0 or y_ >= len(schema) or not schema[y_][x_].isdigit():
            continue

        start = x_
        while schema[y_][start].isdigit():
            start -= 1
        start +=1
        end = x_
        while schema[y_][end].isdigit():
            end += 1

        parts.append(''.join(schema[y_][start:end]))
        for i in range(start, end):
            schema[y_][i] = '.'

    return parts


schema = []
for line in stdin:
    schema.append(list(line))

answer = 0
for y in range(0, len(schema)):
    for x in range(0, len(schema[0])):
        if schema[y][x] == '*':
            parts = get_parts(schema, y, x)
            if parts and len(parts) == 2:
                answer += int(parts[0]) * int(parts[1])

print(answer)
