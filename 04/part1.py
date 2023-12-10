with open("input.txt") as f:
    lines = f.readlines()

answer = 0
for line in lines:
    card, numbers = line.split(":")
    raw_win, raw_number = numbers.split("|")
    winning = {int(x) for x in raw_win.split()}
    my_numbers = {int(x) for x in raw_number.split()}
    count_winning = len(winning.intersection(my_numbers))
    if count_winning:
        answer += 2 ** (count_winning-1)

print(answer)