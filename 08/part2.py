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


current_nodes = [x for x in elements if x[2] == "A"]
steps_by_start = []

# assumes that all the paths loops
node_history = []
for node in current_nodes:
    steps = 0
    current_node = node
    last_important_step = 0

    while current_node[2] != "Z":
        for i in instructions:
            node_history.append(current_node)
            steps += 1
            current_node = elements[current_node][i]
    steps_by_start.append(steps)

print(current_nodes, steps_by_start)

from math import lcm
print(lcm(*steps_by_start))


# Brute force (seems too slow)
# steps = 0
# while True:
#     for i in instructions:
#         steps += 1
#         for k, node in enumerate(current_nodes):
#             current_nodes[k] = elements[current_nodes[k]][i]
#         print(steps, current_nodes, {x[2] for x in current_nodes})
#         if {x[2] for x in current_nodes} == {"Z"}:
#             print(steps)
#             exit()