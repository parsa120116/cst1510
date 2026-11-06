with open("DATA/Les_Brown.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
print(f"The file DATA/Les_Brown.txt has {line_count} lines.")
