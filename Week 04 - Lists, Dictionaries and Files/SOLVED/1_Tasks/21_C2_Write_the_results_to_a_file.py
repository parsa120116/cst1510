def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    try:
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({"label": label, "value": float(value), "limit": float(limit)})
    except FileNotFoundError:
        print(f"Could not find {path}, starting with no records.")
    return records


records = load_records("records_sample.txt")
for record in records:
    status = "OVER LIMIT" if record["value"] > record["limit"] else "OK"
    print(f"{record['label']}: {status}")

print(load_records("nope.txt"))


with open("results.txt", "w") as f:
    for record in records:
        status = "OVER LIMIT" if record["value"] > record["limit"] else "OK"
        f.write(f"{record['label']},{status}\n")

with open("results.txt") as f:
    print(f.read())
