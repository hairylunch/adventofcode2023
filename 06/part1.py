with open("input.txt") as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

counts = []
for time, distance in zip(times, distances):
    ways = 0
    print(time, distance)
    prev_dist = 0
    for hold in range(1, time):
        cur_dist = hold * (time - hold)
        if cur_dist > distance:
            ways += 1
        elif cur_dist < prev_dist:
            break
        prev_dist = cur_dist
    counts.append(ways)

answer = 1
for i in counts:
    answer *= i
print(answer)








