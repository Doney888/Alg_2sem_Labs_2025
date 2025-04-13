class CardsInfo:
    _suits_ = ['S', 'C', 'D', 'H']
    _rangs_ = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    _rangsValue_ = {'6': 0, '7': 1, '8': 2, '9': 3, 'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}

class Card(CardsInfo):
    def __init__(self, suit, rang):
        self.suit = suit
        self.rang = rang

    def __init__(self, s):
        self.suit = s[1]
        self.rang = s[0]

    def __str__(self):
        return f'{self.rang}{self.suit}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rang == other.rang

    def isgreater(self, other, trump):
        return ((self.suit == other.suit and self._rangsValue_[self.rang] > self._rangsValue_[other.rang]) or
                (self.suit != other.suit and self.suit == trump))

def main():
    f = open('input.txt', 'r')
    n, m, trump = map(str, f.readline().split())
    n = int(n)
    m = int(m)
    my_hand = []
    enemy_hand = []
    s = f.readline().split()
    for i in s:
        my_hand.append(Card(i))
    s = f.readline().split()
    for i in s:
        enemy_hand.append(Card(i))
    f.close()

    f = open('output.txt', 'w')
    used_cards = []
    for i in enemy_hand:
        tmp = -1;
        for j in range (len(my_hand)):
            if j in used_cards: continue
            if my_hand[j].isgreater(i, trump):
                if tmp == -1: tmp = j
                elif my_hand[tmp].isgreater(my_hand[j], trump): tmp = j;
        if tmp == -1:
            f.write("NO")
            f.close()
            return
        used_cards.append(tmp)
    f.write("YES")
    f.close()

main()
