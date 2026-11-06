import random

lottery_number = random.randint(0, 99)
lottery = f"{lottery_number:02d}"   # always 2 characters: 7 -> "07"

guess = input("Enter your lottery pick (two digits): ")

if len(guess) != 2 or not guess.isdigit():
    print("Please enter exactly two digits, for example 07 or 45.")
else:
    print(f"The lottery number is {lottery}")

    if guess == lottery:
        print("Exact match: you win £10,000")
    elif sorted(guess) == sorted(lottery):
        print("Match all digits: you win £3,000")
    elif guess[0] in lottery or guess[1] in lottery:
        print("Match one digit: you win £1,000")
    else:
        print("Sorry, no match")
