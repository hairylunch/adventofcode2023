with open("input.txt") as f:
    lines = f.readlines()

seeds = []
# nested list
maps = []
current_map = []
for line in lines:
    if line.strip():
        if line.startswith("seeds"):
            # [dest, source, offset]
            seeds = [int(x) for x in line.split(":")[1].split()]
        elif "map" in line:
            if current_map:
                maps.append(sorted(current_map))
            current_map = []
        else:
            current_map.append([int(x) for x in line.split()])

maps.append(sorted(current_map))
reverse_maps = list(reversed(maps))

seed_ranges = []
for seed_index in range(0, len(seeds), 2):
    seed_ranges.append((seeds[seed_index], seeds[seed_index] + seeds[seed_index+1]))
seed_ranges.sort()

location = -1
while True:
    location += 1
    # print(location)
    mapped_locations = [location]
    for list_of_maps in reverse_maps:
        for lookup in list_of_maps:
            # optimization
            if mapped_locations[-1] < lookup[0]:
                break
            if lookup[0] <= mapped_locations[-1] < lookup[0] + lookup[2]:
                mapped_locations.append(mapped_locations[-1] + lookup[1] - lookup[0])
                break
    # check if starting value is in the list of seeds

    for seed_range in seed_ranges:
        if seed_range[0] <= mapped_locations[-1] < seed_range[1]:
            print(location)
            exit()


