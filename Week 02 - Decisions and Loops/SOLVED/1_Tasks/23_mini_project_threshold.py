# ===== INPUT
label = input("Hostname: ")
value = float(input("GB used: "))
limit = float(input("GB total: "))

# ===== PROCESS
if value > limit:
    status = "OVER LIMIT"
else:
    status = "OK"

# ===== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Used        : {value:.0f}")
print(f"  Total       : {limit:.0f}")
print(f"  Status      : {status}")
print("=" * 34)
