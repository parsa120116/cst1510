import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Hand:
    """The cards held by one player, and their score."""

    def __init__(self):
        """Start with no cards."""
        self.cards = []

    def add_card(self):
        """Deal one random card into this hand."""
        self.cards.append(random.choice(CARDS))

    def score(self):
        """Return this hand's score (0 means blackjack)."""
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0
        total = sum(self.cards)
        aces = self.cards.count(11)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total


# Step 5: test Hand on its own before using it in the game
test = Hand()
test.add_card()
test.add_card()
print(test.cards, test.score())

test.cards = [11, 11, 9]       # two aces: 11+11+9 = 31 -> 21
print(test.cards, test.score())
