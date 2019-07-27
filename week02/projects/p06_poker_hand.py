import collections

deck = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, "J": 11, "Q": 12, "K": 13,
        "A": 14}


def poker_hand(card1, card2):
    p1 = PlayersCard(card1)
    p2 = PlayersCard(card2)
    if p1.rank != p2.rank:
        return winner(p1.rank, p2.rank)
    else:
        if p1.rank == 10 or p1.rank == 9 or p1.rank == 5:
            return winner(p1.numbers[0], p2.numbers[0])
        elif p1.flash:
            return check_list(p1.numbers, p2.numbers)
        elif len(p1.matches) > 0:
            return check_list(p1.match_rank, p2.match_rank)
        else:
            return check_list(p1.numbers, p2.numbers)


class PlayersCard:
    def __init__(self, hand):
        self.card = list(hand.split())
        self.numbers = sorted([deck[x[0:-1]] for x in self.card], reverse=True)
        self.flash = len(list(dict.fromkeys([x[-1] for x in self.card]))) == 1
        self.match = dict(collections.Counter(self.numbers).most_common())
        self.straight = all(self.numbers[i] - self.numbers[i + 1] == 1 for i in range(len(self.numbers)-1))
        self.matches = [x for x in self.match.values() if x > 1]
        self.match_rank = list(self.match.keys())
        if self.flash and self.straight and self.numbers[0] == 14:
            self.rank = 10
        elif self.flash and self.straight:
            self.rank = 9
        elif self.flash:
            self.rank = 6
        elif self.straight:
            self.rank = 5
        elif len(self.matches) > 0:
            if self.matches[0] == 4:
                self.rank = 8
            elif self.matches[0] == 3 and len(self.matches) == 2:
                self.rank = 7

            elif self.matches[0] == 3:
                self.rank = 4
            elif len(self.matches) == 2:
                self.rank = 2
            else:
                self.rank = 1
        else:
            self.rank = 0


def winner(a, b):
    if a > b:
        return "Player 1 WIN"
    elif a < b:
        return "Player 2 WIN"
    else:
        return "Tie"


def check_list(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "Player 1 WIN"
        elif a[i] < b[i]:
            return "Player 2 WIN"
        elif a[i] == b[i] and i == len(a) - 1:
            return "Tie"


print(poker_hand('AH KH QH JH TH', '3S 4D 5C 6H 7D'))
