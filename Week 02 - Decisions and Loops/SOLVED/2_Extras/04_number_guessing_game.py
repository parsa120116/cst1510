secret = 37
guesses = 0

print("I'm thinking of a number between 1 and 100.")
while True:
    guess = int(input("Make a guess: "))
    guesses += 1
    if guess > secret:
        print("Too high.")
    elif guess < secret:
        print("Too low.")
    else:
        print(f"You got it! The answer was {secret}. It took you {guesses} guesses.")
        break
