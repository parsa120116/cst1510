items = []
with open("DATA/clothing_stock.txt") as file:
    for line in file:
        line = line.strip()
        if line != "":                 # skip empty lines
            items.append(line)

items.reverse()

with open("reversed_clothing_stock.txt", "w") as out_file:
    for item in items:
        out_file.write(item + "\n")

print(f"Wrote {len(items)} items in reverse order to reversed_clothing_stock.txt")
print("First 3 lines now:", items[:3])
print("Last 3 lines now:", items[-3:])
