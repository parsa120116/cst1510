# ===== INPUT
dataset_name = input("Dataset name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# ===== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"  Loaded      : {rows_loaded:.0f}")
print(f"  Expected    : {rows_expected:.0f}")
print("=" * 34)
