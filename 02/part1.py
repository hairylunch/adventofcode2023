max_cubes = {"red": 12, "green": 13, "blue": 14}

possible_games = []

with open("input.txt") as f:
    for line in f:
        game_def, games = line.split(":")
        game_no = int(game_def.split()[1])
        # print(game_no)
        draws = games.replace(";", ",").split(",")
        game_possible = True
        for draw in draws:
            cube_count, color = draw.split()
            # print(cube_count, color)
            if int(cube_count) > max_cubes[color]:
                game_possible = False
        if game_possible:
            possible_games.append(game_no)

print(possible_games)
print(sum(possible_games))


