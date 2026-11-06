"""
RECORD CHECK  -  my version
Name  : Parsa
Lane  : IT
Run it:   python template.py
"""

over_limit_count = 0                     # counts OVER LIMIT records in this session

while True:
    # ===== INPUT
    label = input("Hostname (or quit to stop): ")
    if label == "quit":
        break
    value = float(input("GB used: "))
    limit = float(input("GB total: "))

    # ===== PROCESS
    difference = limit - value
    percent = value / limit * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ===== OUTPUT
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
    print()

print(f"Session finished: {over_limit_count} record(s) OVER LIMIT.")
