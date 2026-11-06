import random

lottery_number = random.randint(0, 999)
lottery = f"{lottery_number:03d}"   # always 3 characters: 7 -> "007", 42 -> "042"

guess = input("Enter your lottery pick (three digits): ")

if len(guess) != 3 or not guess.isdigit():
    print("Please enter exactly three digits, for example 007 or 123.")
else:
    print(f"The lottery number is {lottery}")

    if guess == lottery:
        print("Exact match: you win £10,000")
    elif sorted(guess) == sorted(lottery):
        print("Match all digits: you win £3,000")
    elif guess[0] in lottery or guess[1] in lottery or guess[2] in lottery:
        print("Match one digit: you win £1,000")
    else:
        print("Sorry, no match")
