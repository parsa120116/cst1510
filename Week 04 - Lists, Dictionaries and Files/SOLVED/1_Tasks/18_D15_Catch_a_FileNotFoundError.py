try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("missing.txt not found")
