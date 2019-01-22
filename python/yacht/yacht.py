YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: x.count(1)
TWOS = lambda x: x.count(2) * 2
THREES = lambda x: x.count(3) * 3
FOURS = lambda x: x.count(4) * 4
FIVES = lambda x: x.count(5) * 5
SIXES = lambda x: x.count(6) * 6
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and any(x.count(i) == 3 for i in set(x)) else 0
FOUR_OF_A_KIND = lambda x: sum(i * 4 for i in set(x) if x.count(i) > 3)
LITTLE_STRAIGHT = lambda x: 30 if sum(x) == 15 and len(set(x)) == 5 else 0
BIG_STRAIGHT = lambda x: 30 if sum(x) == 20 and len(set(x)) == 5 else 0
CHOICE = lambda x: sum(x)

def score(dice, category):
    return category(dice)
