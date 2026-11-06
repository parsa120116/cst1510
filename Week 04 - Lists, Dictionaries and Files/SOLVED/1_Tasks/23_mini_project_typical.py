def check_record(value, limit):
    """Return the space left, the percentage used and the status."""
    difference = limit - value
    percent = value / limit * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


records = [
    {"label": "srv-01", "value": 87.0, "limit": 120.0},
    {"label": "srv-02", "value": 125.0, "limit": 120.0},
    {"label": "srv-03", "value": 110.0, "limit": 120.0},
]

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)


with open("servers.txt", "w") as f:
    f.write("srv-01,87,120\n")
    f.write("srv-02,125,120\n")
    f.write("srv-03,110,120\n")
    f.write("srv-04,40,120\n")
print("servers.txt created")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


records = load_records("servers.txt")

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)
