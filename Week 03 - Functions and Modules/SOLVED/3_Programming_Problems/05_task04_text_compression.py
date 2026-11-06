def compress_string(text):
    """Return text with each run of a repeated character written as char + count."""
    if text == "":
        return text

    compressed = ""
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = char
            count = 1
    compressed += current_char + str(count)   # add the last run

    if len(compressed) > len(text):
        return text
    return compressed


print(compress_string("aaabbbbcccddeee"))   # a3b4c3d2e3
print(compress_string("Hello"))             # Hello
