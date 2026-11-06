with open("notes.txt", "w") as f:
    f.write("R-001\n")
    f.write("R-002\n")

with open("notes.txt") as f:
    print(f.read())
