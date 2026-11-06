"""
RECORD CHECK  -  my version
Name  : Parsa
Lane  : IT
Run it:   python template.py
Data  :   servers.txt  (one record per line: hostname,GB used,GB total)
"""

# ================================================================ FUNCTIONS
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


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue                      # skip empty lines
            label, value, limit = line.split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


# ===================================================================== STORE
try:
    records = load_records("servers.txt")
except FileNotFoundError:
    print("servers.txt not found - starting with no records.")
    records = []

# ========================================================== PROCESS + OUTPUT
over_limit_count = 0

with open("results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)
        results_file.write(f"{record['label']},{status}\n")
        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"\n{over_limit_count} of {len(records)} record(s) OVER LIMIT. Results saved to results.txt")

with open("results.txt") as f:
    print(f.read())
