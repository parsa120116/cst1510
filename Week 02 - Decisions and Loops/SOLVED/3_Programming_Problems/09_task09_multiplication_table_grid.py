for row in range(10):
    for col in range(10):
        if col == 0:
            print(row * col, end="")
        else:
            print(f"{row * col:4}", end="")
    print(" ")
