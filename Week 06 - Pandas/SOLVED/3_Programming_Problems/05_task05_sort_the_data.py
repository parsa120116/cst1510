import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

# 1. Grade, highest -> lowest, top 5
by_grade = df.sort_values("Grade", ascending=False)
print("Top 5 students by Grade:")
print(by_grade.head(5))

# 2. City A -> Z, and inside each city Grade lowest -> highest
by_city_grade = df.sort_values(["City", "Grade"], ascending=[True, True])
print("\nSorted by City (A-Z), then Grade (low-high), first 10 rows:")
print(by_city_grade[["Name", "City", "Grade"]].head(10))
