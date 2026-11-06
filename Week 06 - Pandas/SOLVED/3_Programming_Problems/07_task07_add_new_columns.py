import pandas as pd

df = pd.read_csv("DATA/students.csv")

# 1. Result: Pass / Fail with apply + lambda
df["Result"] = df["Grade"].apply(lambda grade: "Pass" if grade >= 60 else "Fail")

# 2. Combined_Score = 70% grade + 30% attendance, 1 decimal place
df["Combined_Score"] = (df["Grade"] * 0.7 + df["Attendance"] * 0.3).round(1)

# 3. First 10 rows of the columns we care about
print(df[["Name", "Grade", "Attendance", "Result", "Combined_Score"]].head(10))

# 4. How many passed and how many failed?
result_counts = df["Result"].value_counts()
print("\nPass/Fail counts:")
print(result_counts)
print(f"\nPassed: {result_counts['Pass']}")
print(f"Failed: {result_counts['Fail']}")
