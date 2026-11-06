SPECIAL_CHARACTERS = "@#$%!"


def check_password(password):
    """Score password from 0 to 5, print the score and label, and return the score."""
    if " " in password:
        print(f"{password:<12} REJECTED: a password cannot contain spaces")
        return 0

    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in SPECIAL_CHARACTERS for char in password):
        score += 1

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    print(f"{password:<12} score {score}/5  ->  {label}")
    return score


test_passwords = [
    "hello",
    "Hello123",
    "My Pass!",
    "Str0ng@Pass",
    "12345678"
]

for password in test_passwords:
    check_password(password)
