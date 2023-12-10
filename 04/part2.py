with open("input.txt") as f:
    lines = f.readlines()

winning_cards = {x: 1 for x in range(len(lines))}
winning_cards[0] = 1
for i, line in enumerate(lines):
    card, numbers = line.split(":")
    raw_win, raw_number = numbers.split("|")
    winning = {int(x) for x in raw_win.split()}
    my_numbers = {int(x) for x in raw_number.split()}
    count_winning = len(winning.intersection(my_numbers))
    if count_winning != 0:
        for j in range(count_winning):
            winning_cards[i+j+1] += 1 * (winning_cards[i])

print(sum(winning_cards.values()))

