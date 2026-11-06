name_a = "Instagram"
followers_a = 676       # example numbers, in millions
name_b = "Cristiano Ronaldo"
followers_b = 650
score = 0

while True:
    print(f"A: {name_a}   vs   B: {name_b}")
    guess = input('Who has more followers (millions)? Type "A", "B" or "quit": ').upper()
    if guess == "QUIT":
        break

    if followers_a > followers_b:
        answer = "A"
    else:
        answer = "B"

    if guess == answer:
        score += 1
        print(f"Correct! Score: {score}")
    else:
        print(f"Wrong. Score: {score}")

print(f"Final score: {score}")
