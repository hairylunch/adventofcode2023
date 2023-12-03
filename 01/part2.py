codes = []

substitutions = {"one": "1",
                 "two": "2",
                 "three": "3",
                 "four": "4",
                 "five": "5",
                 "six": "6",
                 "seven": "7",
                 "eight": "8",
                 "nine": "9"}

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    numbers_in_line = []
    for i in range(len(line)):
        if line[i].isnumeric():
            numbers_in_line.append(line[i])
            continue
        for word, number in substitutions.items():
            if i+len(word) <= len(line):
                if line[i:i+len(word)] == word:
                    numbers_in_line.append(number)
                    break
    code = f"{numbers_in_line[0]}{numbers_in_line[-1]}"
    codes.append(int(code))

print(sum(codes))
