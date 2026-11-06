with open("records_sample.txt") as f:
    for line in f:
        label, value, limit = line.strip().split(",")
        value = float(value)
        limit = float(limit)
        print(label, value, limit)
