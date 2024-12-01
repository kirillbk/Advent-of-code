from sys import stdin


value = 0
for line in stdin:
    first = last = None
    for i in range(len(line)):
        if first is None and line[i].isdigit():
            first = line[i]
        if last is None and line[len(line) - i - 1].isdigit():
            last = line[len(line) - i - 1]
    value += int(first + last)

print(value)
