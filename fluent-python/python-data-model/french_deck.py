import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list(('J', 'Q', 'K', 'A'))
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        cards = list()
        for suit in self.suits:
            for rank in self.ranks:
                cards.append(Card(rank, suit))
        self._cards = cards

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(choice(deck))
print(deck[:3])
print(deck[12::13])

card = deck[0]
print(card.rank)
print(card.suit)

for card in deck:
    print(card)
