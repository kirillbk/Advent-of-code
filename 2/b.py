from sys import stdin
from functools import reduce
from operator import mul


answer = 0
for game in stdin:
    game, data = game.split(':')
    game = int(game.split()[1])
    cntr = {'red': 0, 'green': 0, 'blue': 0}
    for cubes in data.split(';'):
        for cube in cubes.split(','):
            n, color = cube.split()
            n = int(n)
            cntr[color] = max(cntr[color], n)

    answer += reduce(mul, cntr.values())

print(answer)
