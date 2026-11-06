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
