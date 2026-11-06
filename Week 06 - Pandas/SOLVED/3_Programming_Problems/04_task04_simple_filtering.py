import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

# 1. Students in London
london = df[df["City"] == "London"]
print(london)
print(f"Students in London: {len(london)}")

# 2. Grade below 65 -> only Name and Grade
low_grades = df[df["Grade"] < 65]
print(f"\nStudents with a grade below 65 ({len(low_grades)}):")
print(low_grades[["Name", "Grade"]])

# 3. How many students in each city?
print("\nStudents per city:")
print(df["City"].value_counts())
