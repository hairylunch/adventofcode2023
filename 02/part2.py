answer = 0

with open("input.txt") as f:
    for line in f:
        cubes = {"red": 0, "green": 0, "blue": 0}
        game_def, games = line.split(":")
        game_no = int(game_def.split()[1])
        # print(game_no)
        draws = games.replace(";", ",").split(",")
        game_possible = True
        for draw in draws:
            cube_count, color = draw.split()
            if int(cube_count) > cubes[color]:
                cubes[color] = int(cube_count)
        print(cubes)

        answer += cubes["red"] * cubes["green"] * cubes["blue"]

print(answer)



