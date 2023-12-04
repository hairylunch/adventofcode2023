def main():
    with open("input.txt") as f:
        lines = f.readlines()

    potential_gears = find_potential_gears(lines)

    potential_part_numbers = find_potential_part_numbers(lines)

    # print(potential_part_numbers, potential_gears)

    sum_of_ratios = 0
    for potential_gear in potential_gears:
        adjacent_part_numbers = []
        row_of_interest = potential_gear[0]
        col_of_interest = potential_gear[1]
        # check for part number above

        for row_number in range(row_of_interest-1, row_of_interest+2):
            if 0 <= row_number <= len(lines)-1:
                for part in potential_part_numbers[row_number]:
                    if part[0]-1 <= col_of_interest <= part[1] + 1:
                        adjacent_part_numbers.append(int(lines[row_number][part[0]:part[1]+1]))
        if len(adjacent_part_numbers) == 2:
            sum_of_ratios += adjacent_part_numbers[0] * adjacent_part_numbers[1]
    print(sum_of_ratios)


def find_potential_part_numbers(lines):
    part_numbers = {}
    line_count = len(lines)
    width = len(lines[0].strip())

    for i in range(line_count):
        line = lines[i].strip()
        start_index = 0
        end_index = 0
        part_numbers[i] = []
        processing_number = False
        for j in range(width):
            # print(line, j,  start_index, end_index, processing_number)
            if line[j].isnumeric():
                if not processing_number:
                    processing_number = True
                    start_index = j
                # end of line or next character is not a num, thus end of the number string
                if j == width - 1 or not line[j + 1].isnumeric():
                    processing_number = False
                    end_index = j
                    part_numbers[i].append((start_index, end_index))

    return part_numbers

def find_potential_gears(lines):
    potential_gears = []
    row_count = len(lines)
    width = len(lines[0].strip())

    for i in range(row_count):
        line = lines[i].strip()
        for j in range(width):
            if line[j] == "*":
                potential_gears.append((i, j))
    return potential_gears


if __name__ == "__main__":
    main()

