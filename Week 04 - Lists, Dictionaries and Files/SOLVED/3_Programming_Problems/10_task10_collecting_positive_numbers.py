numbers = []

while True:
    entry = input('Enter a positive number (or type "done" to stop): ').strip()
    if entry.lower() == "done":
        break
    if entry.isdigit() and int(entry) > 0:
        numbers.append(int(entry))
    else:
        print("That is not a positive whole number. Try again.")

if len(numbers) > 0:
    print("Numbers entered:", numbers)
    found_even = False
    for number in numbers:
        if number % 2 == 0:
            print("First even number:", number)
            found_even = True
            break
    if not found_even:
        print("No even numbers found")
else:
    print("No numbers were entered")
