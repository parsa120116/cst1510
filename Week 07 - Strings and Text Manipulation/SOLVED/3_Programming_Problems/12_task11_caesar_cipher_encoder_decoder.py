def encode(text, key):
    """Return text with every letter a-z / A-Z shifted forward by key places."""
    result = ""
    for char in text:
        if not char.isalpha():
            result += char              # space, digit, punctuation: unchanged
            continue

        if char.isupper():
            base = ord("A")             # 65
        else:
            base = ord("a")             # 97

        position = ord(char) - base     # 'a' -> 0, 'b' -> 1, ... 'z' -> 25
        new_position = (position + key) % 26
        result += chr(base + new_position)
    return result


def decode(text, key):
    """Return text with every letter shifted back by key places (undoes encode)."""
    return encode(text, -key)


original = "Hello World! 123"
key = 5

secret = encode(original, key)
back = decode(secret, key)

print(f"Original: {original}")
print(f"Encoded:  {secret}")
print(f"Decoded:  {back}")
print(f"decode(encode(text, key), key) == text? {back == original}")

print()
print(encode("xyz XYZ", 3))        # wrap-around check: abc ABC
print(decode("abc ABC", 3))        # and back: xyz XYZ
