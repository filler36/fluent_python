from collections import namedtuple
from random import choice

"""
Although FrenchDeck implicitly inherits from object, its functionality is not inherited, but comes from leveraging
the data model and composition. By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like
a standard Python sequence, allowing it to benefit from core language features (e.g., iteration and slicing) and from
the standard library, as shown by the examples using random.choice, reversed, and sorted. Thanks to composition,
the __len__ and __getitem__ implementations can hand off all the work to a list object, self._cards.
"""

Card = namedtuple('Card', ['rank', 'suit'])


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    suits = 'spades diamonds clubs hearts'.split()  # => ['spades', 'diamonds', 'clubs', 'hearts']
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # => ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        """ [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), ... ] """
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """
        Implement special syntax obj[key]
        Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing.
        by implementing the __getitem__ special method, our deck is also iterable
        """
        return self._cards[position]


deck = FrenchDeck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# Print cards in sorted order
for card in sorted(deck, key=spades_high):
    print(card)

# Get random card
print(choice(deck))

# Get three cards from the top
print(deck[:3])

# Get aces
print(deck[12::13])

# The deck can also be iterated in reverse
for card in reversed(deck):
    print(card)

# If a collection has no __contains__ method, the in operator does a sequential scan.
# "in" works with our FrenchDeck class because it is iterable.
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)
