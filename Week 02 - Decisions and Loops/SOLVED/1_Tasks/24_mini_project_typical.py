# ===== INPUT
label = input("Hostname: ")
value = float(input("GB used: "))
limit = float(input("GB total: "))

# ===== PROCESS
difference = limit - value              # GB still free
percent = value / limit * 100           # how full the disk is

if percent >= 100:
    status = "OVER LIMIT"
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
