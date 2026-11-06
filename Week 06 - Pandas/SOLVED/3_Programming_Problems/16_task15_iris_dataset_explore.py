import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/iris_dataset.csv")

# 1. First look
print(df.head())
print("\nShape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df.describe())

# 2. Flowers per species
print("\nFlowers per species:")
print(df["target"].value_counts())

# 3. Missing values and duplicated rows
print("\nMissing values per column:")
print(df.isna().sum())
print(f"Total missing values: {df.isna().sum().sum()}")

duplicate_count = df.duplicated().sum()
print(f"\nDuplicated rows: {duplicate_count}")
print("All copies of the repeated rows:")
print(df[df.duplicated(keep=False)])
