def check_for_adjacent_symbol(row, start, end):
    # check the row above
    if row != 0:
        line_above = lines[row-1].strip()
        for i in range(max(0, start_index-1), min(width, end_index+2)):
            if is_symbol(line_above[i]):
                return True
    # check the before and after
    number_line = lines[row].strip()
    if start != 0:
        if is_symbol(number_line[start_index-1]):
            return True
    if end != width-1:
        if is_symbol(number_line[end_index+1]):
            return True
    # check the row below
    if row != len(lines)-1:
        line_below = lines[row+1].strip()
        # range is not inclusive, hence the max is +2
        for i in range(max(0, start_index-1), min(width, end_index+2)):
            if is_symbol(line_below[i]):
                return True
    return False


def is_symbol(i):
    if not (i.isnumeric() or i == "."):
        return True
    return False

lines = []
with open("input.txt") as f:
    lines = f.readlines()

part_numbers = []
line_count = len(lines)
width = len(lines[0].strip())

for i in range(line_count):
    line = lines[i].strip()
    start_index = 0
    end_index = 0
    processing_number = False
    for j in range(width):
        # print(line, j,  start_index, end_index, processing_number)
        if line[j].isnumeric():
            if not processing_number:
                processing_number = True
                start_index = j
                # check if it's a single digit number
            # end of line or next character is not a num, thus end of the number string
            if j == width-1 or not line[j+1].isnumeric():
                processing_number = False
                end_index = j
                is_part = check_for_adjacent_symbol(i, start_index, end_index)
                if is_part:
                    part_numbers.append(int(line[start_index:end_index+1]))

print(part_numbers)
print(sum(part_numbers))




