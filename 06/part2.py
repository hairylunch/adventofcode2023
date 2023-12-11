with open("input.txt") as f:
    lines = f.readlines()


time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

ways=0
ways = 0
prev_dist = 0
for hold in range(1, time):
    cur_dist = hold * (time - hold)
    if cur_dist > distance:
        ways += 1
    elif cur_dist < prev_dist:
        break
    prev_dist = cur_dist

print(ways)








