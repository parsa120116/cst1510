actual_password = "MDX123"

guess = input("Enter your password guess: ")

if guess == actual_password:
    print("Password cracked!")
else:
    matches = 0
    for i in range(len(actual_password)):
        # Same position, same character (and same case)?
        if i < len(guess) and guess[i] == actual_password[i]:
            matches += 1

    # A longer guess should not get 100%, so divide by the longer length
    total_positions = len(actual_password)
    if len(guess) > total_positions:
        total_positions = len(guess)

    accuracy = round(matches / total_positions * 100)
    print(f"Accuracy: {accuracy}%")
