total = 0

while True:
    answer = input("Enter a number (or done to finish): ")
    if answer == "done":
        break
    total += float(answer)

print("Total:", total)
