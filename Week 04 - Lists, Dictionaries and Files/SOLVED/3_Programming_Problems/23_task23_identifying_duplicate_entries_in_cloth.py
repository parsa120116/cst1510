seen = set()          # every (item, size) we have met so far
duplicates = set()    # the ones we met more than once

with open("DATA/clothing_stock.txt") as file:
    for line in file:
        if line.strip() == "":
            continue
        item, size = line.split(",")
        entry = (item.strip(), size.strip())    # e.g. ("Hoodie", "XS")
        if entry in seen:
            duplicates.add(entry)
        else:
            seen.add(entry)

if len(duplicates) > 0:
    print(f"{len(duplicates)} duplicate entries found:")
    for item, size in sorted(duplicates):
        print(f"- {item}, {size}")
else:
    print("No duplicates found.")
