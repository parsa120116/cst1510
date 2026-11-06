import pandas as pd

# Display settings: show every column side by side (no "..." and no wrapping)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 3 rows:")
print(df.tail(3))

print("\nShape:", df.shape)
print("Rows:", df.shape[0], "| Columns:", df.shape[1])

print("Columns:", df.columns.tolist())
