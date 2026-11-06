import pandas as pd

df = pd.read_csv("DATA/students.csv")

# 1. (CS or DS) AND Grade > 75 AND Attendance > 80
strong_students = df[
    (df["Course"].isin(["Computer Science", "Data Science"]))
    & (df["Grade"] > 75)
    & (df["Attendance"] > 80)
]
print(f"CS/DS students with Grade > 75 and Attendance > 80: {len(strong_students)}")
print(strong_students[["Name", "Course", "Grade", "Attendance"]])

# 2. At risk of failing: Grade < 60
at_risk = df[df["Grade"] < 60]
print(f"\nStudents at risk of failing (Grade < 60): {len(at_risk)}")
print(at_risk[["Name", "Grade"]])

# 3. Scholarship students from Manchester with Grade > 80
manchester_scholars = df[
    (df["Scholarship"] == "Yes")
    & (df["City"] == "Manchester")
    & (df["Grade"] > 80)
]
print(f"\nManchester scholarship students with Grade > 80: {len(manchester_scholars)}")
print(manchester_scholars[["Name", "Grade", "Scholarship"]])
