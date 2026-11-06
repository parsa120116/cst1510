text = "abc"

try:
    number = float(text)
    print(number)
except ValueError:
    print(f"Not a number: {text}")
