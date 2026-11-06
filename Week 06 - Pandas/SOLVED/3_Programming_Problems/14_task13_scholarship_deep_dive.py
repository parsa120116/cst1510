import pandas as pd

df = pd.read_csv("DATA/students.csv")

# A 1/0 helper column: 1 = has a scholarship, 0 = does not
df["Has_Scholarship"] = df["Scholarship"].apply(lambda s: 1 if s == "Yes" else 0)

# 1. Percentage of all students with a scholarship
scholars = df["Has_Scholarship"].sum()
percent_scholars = scholars / len(df) * 100
print(f"1) {scholars} of {len(df)} students have a scholarship ({percent_scholars:.1f}%)")

# 2. Average grade: scholarship vs non-scholarship
grade_by_scholarship = df.groupby("Scholarship")["Grade"].mean()
grade_yes = grade_by_scholarship["Yes"]
grade_no = grade_by_scholarship["No"]
print(f"\n2) Average Grade - scholarship: {grade_yes:.1f}, no scholarship: {grade_no:.1f}")
print(f"   Difference: {grade_yes - grade_no:.1f} points -> a big, meaningful gap")

# 3. Per course: total, with scholarship, rate (%)
course_table = df.groupby("Course").agg(
    Total_Students=("Name", "count"),
    With_Scholarship=("Has_Scholarship", "sum"),
)
course_table["Scholarship_Rate"] = (
    course_table["With_Scholarship"] / course_table["Total_Students"] * 100
).round(1)
course_table = course_table.sort_values("Scholarship_Rate", ascending=False)
print("\n3) Scholarships per course:")
print(course_table)

# 4. Attendance: scholarship vs non-scholarship
attendance_by_scholarship = df.groupby("Scholarship")["Attendance"].mean()
att_yes = attendance_by_scholarship["Yes"]
att_no = attendance_by_scholarship["No"]
print(f"\n4) Average Attendance - scholarship: {att_yes:.1f}%, no scholarship: {att_no:.1f}%")
print(f"   Difference: {att_yes - att_no:.1f} points")

# 5. SUMMARY
# 10 of the 25 students (40%) have a scholarship. Scholarship students average
# 86.1 against 69.5 for the rest (16.6 points higher) and also attend more
# (90.1% against 75.5%), so the awards do go to strong, committed students.
# Mathematics has the highest scholarship rate (66.7%) and Data Science the lowest
# (16.7%, only Oliver Price), even though Data Science has other strong students
# such as Priya Shah (84) - that is worth a second look.
