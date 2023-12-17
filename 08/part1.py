with open("input.txt") as f:
    raw_instructions = f.readline()
    # skip the blank line
    f.readline()
    lines = f.readlines()

instructions = []
for i in raw_instructions.strip():
    if i == "L":
        instructions.append(0)
    else:
        instructions.append(1)

elements = {}
for line in lines:
    first_split = line.strip().split("=")
    key = first_split[0].strip()
    left = first_split[1][2:5]
    right = first_split[1][7:10]
    elements[key] = [left, right]

current_node = "AAA"
steps = 0
while True:
    for i in instructions:
        current_node = elements[current_node][i]
        steps += 1
        if current_node == "ZZZ":
            print(steps)
            exit()
