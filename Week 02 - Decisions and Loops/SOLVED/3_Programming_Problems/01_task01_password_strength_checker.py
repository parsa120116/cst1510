password = input("Enter a password: ")
length = len(password)

# Check the strongest rule first: 12+ is also 8+
if length >= 12:
    print("Strong")
elif length >= 8:
    print("Moderate")
else:
    print("Weak")
