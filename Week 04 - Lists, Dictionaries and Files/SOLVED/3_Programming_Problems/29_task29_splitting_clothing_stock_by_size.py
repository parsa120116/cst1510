size_order = ["XS", "S", "M", "L", "XL", "XXL"]
items_by_size = {}      # size -> set of items in that size

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if line.strip() == "":
            continue
        item, size = line.split(",")
        item = item.strip()
        size = size.strip()
        if size not in items_by_size:
            items_by_size[size] = set()
        items_by_size[size].add(item)

for size in size_order:
    if size in items_by_size:
        items = items_by_size[size]
        print(f"{size} ({len(items)} items): {sorted(items)}")

# Any size that is not in our list (just in case the file has one)
for size in items_by_size:
    if size not in size_order:
        print(f"{size} ({len(items_by_size[size])} items): {sorted(items_by_size[size])}")
