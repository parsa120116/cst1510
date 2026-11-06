import random

word_list = ["apple", "banana", "camel", "python", "string", "letter", "puzzle", "london"]

chosen_word = random.choice(word_list)
lives = 6
guessed_letters = []

# Step 2: one underscore per letter, e.g. "apple" -> "_ _ _ _ _"
placeholder = ""
for letter in chosen_word:
    placeholder += "_ "
print("Welcome to Hangman!")
print(placeholder.strip())

# The display is a list, so we can change one position at a time
display = []
for letter in chosen_word:
    display.append("_")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type exactly one letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    print(" ".join(display))
    print(f"Lives left: {lives}")

if "_" not in display:
    print(f"You win! The word was '{chosen_word}'.")
else:
    print(f"You lose! The word was '{chosen_word}'.")
