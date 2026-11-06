sizes_per_item = {}     # item -> set of its sizes

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if line.strip() == "":
            continue
        item, size = line.split(",")
        item = item.strip()
        size = size.strip()
        if item not in sizes_per_item:
            sizes_per_item[item] = set()      # first time we see this item
        sizes_per_item[item].add(size)

size_counts = {}
for item, sizes in sizes_per_item.items():
    size_counts[item] = len(sizes)

print(size_counts)
