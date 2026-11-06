import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students_missing.csv")
print(f"Rows before cleaning: {len(df)}")

# 1. Missing values in each column
print("\nMissing values per column:")
print(df.isna().sum())

# 2. Rows with at least one missing value
rows_with_missing = df[df.isna().any(axis=1)]
print(f"\nRows with at least one missing value ({len(rows_with_missing)}):")
print(rows_with_missing)

# 3. Fix the missing values (always save the result back with =)
grade_average = round(df["Grade"].mean(), 1)
print(f"\nAverage Grade used to fill the gaps: {grade_average}")
df["Grade"] = df["Grade"].fillna(grade_average)
df["Scholarship"] = df["Scholarship"].fillna("Unknown")
df["Course"] = df["Course"].fillna("Unknown")
df = df.dropna(subset=["Attendance"])
df = df.dropna(subset=["Age"])

# NaN had turned Age and Attendance into decimals (18.0); make them whole numbers again
df["Age"] = df["Age"].astype(int)
df["Attendance"] = df["Attendance"].astype(int)

# 4. Check: no missing values left
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print(f"Total missing: {df.isnull().sum().sum()}")
print(f"Rows after cleaning: {len(df)}")

# 5. Save without the index
df.to_csv("DATA/students_clean.csv", index=False)
print("\nSaved DATA/students_clean.csv")
