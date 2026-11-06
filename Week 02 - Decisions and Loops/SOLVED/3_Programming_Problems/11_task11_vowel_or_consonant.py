letter = input("Enter a letter: ").lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f"{letter} is a vowel.")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print(f"{letter} is a consonant.")
