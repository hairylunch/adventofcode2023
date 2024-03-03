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
loop_coords = [start]
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
        break
    distance += 1
    loop_coords.append(next_coords)
    prev_coords = current_coords
    current_coords = next_coords
    next_coords = find_next_coords(current_coords, prev_coords)

# find the maximum dimensions of the loop
min_row = min([x[0] for x in loop_coords])
max_row = max([x[0] for x in loop_coords])
min_col = min([x[1] for x in loop_coords])
max_col = max([x[1] for x in loop_coords])

# walk the grid and ray trace for the points
# this was surprisingly slow - would be worth a revisit if doing again
inside_points = 0
vertical_crossings = [{"L", "7"}, {"F", "J"}]
for row in range(min_row, max_row):
    for col in range(min_col, max_col):
        intersections = 0
        corners = set()
        if [row, col] not in loop_coords:
            for col_to_check in range(col+1, len(grid[0])):
                # print([row, col], col_to_check)
                if [row, col_to_check] in loop_coords and grid[row][col_to_check] != "-":
                    # only count when you cross a | or two corners that result in a vertical crossing ({"L","7"} or {"F", "J"}
                    if grid[row][col_to_check] == "|":
                        intersections += 1
                    else:
                        corners.add(grid[row][col_to_check])
                        if len(corners) == 2:
                            if corners in vertical_crossings:
                                intersections += 1
                            corners = set()

            # print([row, col], col_to_check, intersections)
            if (intersections) % 2 == 1:
                inside_points += 1
print (inside_points)
