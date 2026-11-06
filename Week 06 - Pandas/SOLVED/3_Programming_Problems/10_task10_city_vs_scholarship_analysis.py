import pandas as pd

df = pd.read_csv("DATA/students.csv")

# 1. Number of students per city
print("1) Students per city:")
print(df.groupby("City")["Name"].count())

# 2. Average grade per city, highest first
city_grade = df.groupby("City")["Grade"].mean().round(1)
print("\n2) Average Grade per city (highest first):")
print(city_grade.sort_values(ascending=False))

# 3. Average grade: scholarship vs no scholarship
scholarship_grade = df.groupby("Scholarship")["Grade"].mean().round(1)
print("\n3) Average Grade by Scholarship:")
print(scholarship_grade)
gap = scholarship_grade["Yes"] - scholarship_grade["No"]
print(f"Scholarship students score {gap:.1f} points higher on average.")

# 4. Count by City AND Scholarship
city_scholarship = df.groupby(["City", "Scholarship"])["Name"].count()
print("\n4) Students per City and Scholarship:")
print(city_scholarship)

scholars_per_city = df[df["Scholarship"] == "Yes"]["City"].value_counts()
print("\nScholarship students per city:")
print(scholars_per_city)
print(f"Most scholarship students: {scholars_per_city.index[0]} ({scholars_per_city.iloc[0]})")
