def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# INPUT
label = input("Hostname: ")
value = float(input("GB used: "))
limit = float(input("GB total: "))

# PROCESS
difference = limit - value
percent = value / limit * 100
status = status_of(percent)

# OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Used        : {value:.0f}")
print(f"  Total       : {limit:.0f}")
print(f"  Status      : {status}")
print("=" * 34)
