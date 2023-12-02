from sys import stdin


answer = 0
for game in stdin:
    game, data = game.split(':')
    game = int(game.split()[1])

    is_game_valid = True
    for cubes in data.split(';'):
        for cube in cubes.split(','):
            n, color = cube.split()
            n = int(n)
            # 12 red cubes, 13 green cubes, and 14 blue cubes
            if color == 'red' and n > 12:
                is_game_valid = False
            elif color == 'green' and n > 13:
                is_game_valid = False
            elif color == 'blue' and n > 14:
                is_game_valid = False
            if not is_game_valid:
                break

    if is_game_valid:
        answer += game

print(answer)
