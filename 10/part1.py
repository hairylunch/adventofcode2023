with open("input.txt") as f:
    lines = f.readlines()

grid = [[] for i in lines]

start = ()

for row, row_data in enumerate(lines):
    for col, col_value in enumerate(row_data):
        grid[row].append(col_value)
        if col_value == "S":
            start = (row, col)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

print(grid, start)pwd