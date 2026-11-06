# ===== INPUT
dataset_name = input("Dataset name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# ===== PROCESS
rows_missing = rows_expected - rows_loaded
percent_loaded = rows_loaded / rows_expected * 100

# ===== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"  Loaded      : {rows_loaded:>10.2f}")
print(f"  Expected    : {rows_expected:>10.2f}")
print(f"  Missing     : {rows_missing:>10.2f}")
print(f"  Percent     : {percent_loaded:>10.2f} %")
print("=" * 34)
