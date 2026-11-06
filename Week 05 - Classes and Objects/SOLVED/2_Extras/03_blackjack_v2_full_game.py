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


def compare(user_score, computer_score):
    """Return the result message."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


user_hand = Hand()
computer_hand = Hand()
for _ in range(2):
    user_hand.add_card()
    computer_hand.add_card()

game_over = False
while not game_over:
    print(f"Your cards: {user_hand.cards}, current score: {user_hand.score()}")
    print(f"Computer's first card: {computer_hand.cards[0]}")
    if user_hand.score() == 0 or user_hand.score() > 21 or computer_hand.score() == 0:
        game_over = True
    elif input("Type 'y' to get another card, 'n' to pass: ") == "y":
        user_hand.add_card()
    else:
        game_over = True

while computer_hand.score() != 0 and computer_hand.score() < 17:
    computer_hand.add_card()

print(f"Your final hand: {user_hand.cards}, final score: {user_hand.score()}")
print(f"Computer's final hand: {computer_hand.cards}, final score: {computer_hand.score()}")
print(compare(user_hand.score(), computer_hand.score()))
