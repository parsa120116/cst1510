import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password? "))
n_symbols = int(input("How many symbols would you like? "))
n_numbers = int(input("How many numbers would you like? "))

# Easy version: in order
easy = ""
for _ in range(n_letters):
    easy += random.choice(letters)
for _ in range(n_symbols):
    easy += random.choice(symbols)
for _ in range(n_numbers):
    easy += random.choice(numbers)
print(f"Easy password: {easy}")

# Hard version: shuffled
chars = []
for _ in range(n_letters):
    chars.append(random.choice(letters))
for _ in range(n_symbols):
    chars.append(random.choice(symbols))
for _ in range(n_numbers):
    chars.append(random.choice(numbers))
random.shuffle(chars)
hard = "".join(chars)
print(f"Hard password: {hard}")
