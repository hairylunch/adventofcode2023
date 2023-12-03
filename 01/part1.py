codes = []

with open("input.txt") as f:
    for line in f:
        numbers_in_line = []
        for i in line:
            if i.isnumeric():
                numbers_in_line.append(i)
        code = f"{numbers_in_line[0]}{numbers_in_line[-1]}"
        print(line, numbers_in_line, code)
        codes.append(int(code))

print(sum(codes))
