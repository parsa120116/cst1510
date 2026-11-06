while True:
    text = input("Enter a whole number: ")
    try:
        number = int(text)
        break                       # only reached if int() worked
    except ValueError:
        print(f"Sorry, '{text}' is not a whole number. Please try again.")

print(f"{number} squared is {number ** 2}")
