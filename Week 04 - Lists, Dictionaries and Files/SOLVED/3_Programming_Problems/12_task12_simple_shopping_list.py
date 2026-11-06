items = ["Milk", "Eggs", "Bread", "Apples", "Rice"]

# 1. Write the list to the file, one item per line
with open("shopping.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

# 2 and 3. Read the file, print each item and count them
count = 0
with open("shopping.txt", "r") as file:
    for line in file:
        item = line.strip()
        if item != "":
            print(f"You need to buy: {item}")
            count += 1

print(f"Total number of items: {count}")
