"""
RECORD CHECK  -  my version
Name  : Parsa
Lane  : AI / Data Science
Run it:   python template.py
"""

# ===== INPUT
dataset_name = input("Dataset name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# ===== PROCESS
row_difference = rows_loaded - rows_expected          # negative = rows were lost
percent_loaded = rows_loaded / rows_expected * 100
# Extra line: the share of the data that is MISSING.
# Why: before training a model you must know how much data is lost;
# if too much is missing, the results could be biased.
percent_missing = 100 - percent_loaded

# ===== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"  Loaded      : {rows_loaded:>10.2f}")
print(f"  Expected    : {rows_expected:>10.2f}")
print(f"  Difference  : {row_difference:>+10.2f}")
print(f"  Complete    : {percent_loaded:>10.2f} %")
print(f"  Missing     : {percent_missing:>10.2f} %")
print("=" * 34)
