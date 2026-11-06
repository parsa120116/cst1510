def is_palindrome(text):
    """Return True if text reads the same backward as forward."""
    cleaned = text.lower()
    return cleaned == cleaned[::-1]


words = ["civic", "radar", "level", "rotor", "kayak", "madam", "refer",
         "rotator", "deified", "racecar", "reviver", "Level", "python"]
for word in words:
    print(f"{word}: {is_palindrome(word)}")

user_word = input("Type a word to check: ")
print(is_palindrome(user_word))
