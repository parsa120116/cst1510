alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(original_text, shift_amount):
    """Return original_text with every letter shifted forward by shift_amount."""
    cipher_text = ""
    for char in original_text:
        lower_char = char.lower()
        if lower_char in alphabet:
            position = alphabet.index(lower_char)
            new_position = (position + shift_amount) % 26
            new_char = alphabet[new_position]
            if char.isupper():
                new_char = new_char.upper()
            cipher_text += new_char
        else:
            cipher_text += char          # space, digit, punctuation: keep it
    return cipher_text


def decrypt(original_text, shift_amount):
    """Return original_text with every letter shifted backward by shift_amount."""
    return encrypt(original_text, shift_amount * -1)


def caesar(direction, text, shift):
    """Call encrypt or decrypt depending on direction ('encode' or 'decode')."""
    if direction == "encode":
        return encrypt(text, shift)
    else:
        return decrypt(text, shift)


print("Welcome to the Caesar Cipher!")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    if direction != "encode" and direction != "decode":
        print("Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n")

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("The shift must be a whole number. Let's start again.")
        continue

    result = caesar(direction, text, shift)
    print(f"Here is the {direction}d result: {result}")

    again = input("Type 'yes' to go again. Otherwise, type 'no':\n").strip().lower()
    if again != "yes":
        should_continue = False
        print("Goodbye!")
