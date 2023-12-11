import collections

with open("input.txt") as f:
    lines = f.readlines()

hands_and_bets = []
card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
base_rank = 15 ** 5 + 1
hand_ranks = {
    "five": base_rank * 6,
    "four": base_rank * 5,
    "full": base_rank * 4,
    "three": base_rank * 3,
    "two": base_rank * 2,
    "one": base_rank,
    "high": 0,
}

def raw_card_value(cards):
    i = 0
    value = 0
    for card in reversed(cards):
        value += card_ranks[card] * (15 ** i)
        i += 1
    return value

def cards_to_rank(cards):
    counter = collections.Counter(cards)
    rank = raw_card_value(cards)
    hand = None
    card_counts = counter.most_common()
    if card_counts[0][1] == 5:
        hand = "five"
        rank += hand_ranks[hand]
    elif card_counts[0][1] == 4:
        hand = "four"
        rank += hand_ranks[hand]
    elif card_counts[0][1] == 3:
        if card_counts[1][1] == 2:
            hand = "full"
            rank += hand_ranks[hand]
        else:
            hand = "three"
            rank += hand_ranks[hand]
    elif card_counts[0][1] == 2:
        if card_counts[1][1] == 2:
            hand = "two"
            rank += hand_ranks[hand]
        else:
            hand = "one"
            rank += hand_ranks[hand]
    else:
        hand = "high"
    return rank, hand

ranks_and_bets = []
for line in lines:
    raw_cards, raw_bet = line.split()
    bet = int(raw_bet)
    cards = [x for x in raw_cards]
    rank, hand = cards_to_rank(cards)
    ranks_and_bets.append((rank, bet, hand, cards))


winnings = 0
for i, rank_and_bet in enumerate(sorted(ranks_and_bets)):
    print(rank_and_bet)
    winnings += (i+1) * rank_and_bet[1]

print(winnings)










