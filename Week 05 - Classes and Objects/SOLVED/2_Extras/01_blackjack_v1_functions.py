import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   # 11 = ace, 10s = 10/J/Q/K


def deal_card():
    """Return a random card value."""
    return random.choice(CARDS)


def calculate_score(cards):
    """Return the score of a list of cards (0 means blackjack)."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    total = sum(cards)
    aces = cards.count(11)
    while total > 21 and aces > 0:
        total -= 10          # count one ace as 1 instead of 11
        aces -= 1
    return total


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


user_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]

game_over = False
while not game_over:
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or user_score > 21 or calculate_score(computer_cards) == 0:
        game_over = True
    else:
        if input("Type 'y' to get another card, 'n' to pass: ") == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

computer_score = calculate_score(computer_cards)
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(calculate_score(user_cards), computer_score))
