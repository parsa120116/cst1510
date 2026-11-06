stock = []
with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if line.strip() == "":
            continue
        item, size = line.split(",")
        stock.append((item.strip(), size.strip()))

seen = set()
unique_stock = []
for entry in stock:
    if entry not in seen:        # first time we meet this (item, size)
        seen.add(entry)
        unique_stock.append(entry)

with open("unique_clothing_stock.txt", "w") as out_file:
    for item, size in unique_stock:
        out_file.write(f"{item}, {size}\n")

print(f"Entries in the file:  {len(stock)}")
print(f"Unique entries:       {len(unique_stock)}")
print(f"Duplicates removed:   {len(stock) - len(unique_stock)}")
