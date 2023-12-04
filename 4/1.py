from sys import stdin


answer = 0
for line in stdin:
    _, numbers = line.split(':')
    winning, total = numbers.split('|')
    winning = map(int, winning.split())
    winning = set(winning)
    total = map(int, total.split())
    total = set(total)

    matches = len(total.intersection(winning))
    if matches != 0:
        answer += 2**(matches - 1)

print(answer)
