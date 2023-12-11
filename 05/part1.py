with open("input.txt") as f:
    lines = f.readlines()

seeds = []
# nested list
maps = []
current_map = []
for line in lines:
    if line.strip():
        if line.startswith("seeds"):
            seeds = [int(x) for x in line.split(":")[1].split()]
        elif "map" in line:
            if current_map:
                maps.append(current_map)
            current_map = []
        else:
            current_map.append([int(x) for x in line.split()])
maps.append(current_map)

locations = []
for seed in seeds:
    i = seed
    for list_of_maps in maps:
        # print(seed, list_of_maps, i)
        for lookup in list_of_maps:
            if lookup[1] <= i < lookup[1] + lookup[2]:
                # print ("match!", lookup)
                i = lookup[0] + (i - lookup[1])
                break
    locations.append(i)

print(min(locations))

