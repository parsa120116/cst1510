import random

secret = random.randint(1, 100)
tries = 0
guess = 0   # any value that can't be the secret, so the loop starts

print("I'm thinking of a number between 1 and 100.")

while guess != secret:
    guess = int(input("Your guess: "))
    tries += 1

    if guess > secret:
        print("Too large!")
    elif guess < secret:
        print("Too small!")

print(f"Correct! The number was {secret}.")
print(f"You needed {tries} tries.")
