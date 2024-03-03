with open("input.txt") as f:
    lines = f.readlines()

grid = [[] for i in lines]

start = ()

pipes = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    ".": [],
    "S": [],
}

# direction to look, and the direction you came from
adjacent_offsets = [
    [[0, 1], "W"],
    [[1, 0], "N"],
    [[0, -1], "E"],
    [[-1, 0], "S"],
]


def find_prev_dir(offset: list[int]) -> str:
    for known_offset in adjacent_offsets:
        if known_offset[0] == offset:
            return known_offset[1]


def find_next_coords(current_coords: list[int], prev_coords: list[int]) -> list[int]:
    offset_from_prev = [current_coords[i] - prev_coords[i] for i in range(2)]
    # start (1,1)  new (1,0) - offset would be (0, -1)
    prev_dir = find_prev_dir(offset_from_prev)
    current_pipe = grid[current_coords[0]][current_coords[1]]
    open_ends = pipes[current_pipe]

    if open_ends.index(prev_dir) == 0:
        dir_to_go = open_ends[1]
    else:
        dir_to_go = open_ends[0]

    if dir_to_go == "N":
        return [current_coords[0] - 1, current_coords[1]]
    elif dir_to_go == "S":
        return [current_coords[0] + 1, current_coords[1]]
    elif dir_to_go == "E":
        return [current_coords[0], current_coords[1] + 1]
    elif dir_to_go == "W":
        return [current_coords[0], current_coords[1] - 1]


# find start
for row, row_data in enumerate(lines):
    for col, col_value in enumerate(row_data):
        grid[row].append(col_value)
        if col_value == "S":
            start = [row, col]

distance = 0
# find a starting direction
for offset_details in adjacent_offsets:
    next_coords = [start[i] + offset_details[0][i] for i in range(2)]
    from_dir = offset_details[1]
    pipe = grid[next_coords[0]][next_coords[1]]
    if from_dir in pipes[pipe]:
        distance += 1
        break

current_coords = start
while(True):
    if next_coords == start:
        print(int(distance/2))
        exit()
    prev_coords = current_coords
    current_coords = next_coords
    print("pre", current_coords, prev_coords)
    next_coords = find_next_coords(current_coords, prev_coords)
    distance += 1
    print(next_coords)


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

