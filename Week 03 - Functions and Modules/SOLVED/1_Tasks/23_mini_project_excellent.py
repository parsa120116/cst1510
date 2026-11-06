"""
RECORD CHECK  -  my version
Name  : Parsa
Lane  : IT
Run it:   python template.py
"""

# ================================================================ FUNCTIONS
def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the space left and the percentage used."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent


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


# ===================================================================== MAIN
over_limit_count = 0

while True:
    # INPUT
    label = input("Hostname (or quit to stop): ")
    if label == "quit":
        break
    value = float(input("GB used: "))
    limit = float(input("GB total: "))

    # PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1

    # OUTPUT
    print_report(label, value, limit, difference, percent, status)

print(f"Session finished: {over_limit_count} record(s) OVER LIMIT.")
