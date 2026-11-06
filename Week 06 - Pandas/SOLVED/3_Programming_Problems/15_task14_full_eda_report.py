import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

# Helper columns: 1/0 flags make percentages easy (the mean of 1s and 0s = a fraction)
df["Passed"] = df["Grade"].apply(lambda g: 1 if g >= 60 else 0)
df["Has_Scholarship"] = df["Scholarship"].apply(lambda s: 1 if s == "Yes" else 0)

# 1. Most popular course
course_counts = df["Course"].value_counts()
print(f"1) Most popular course: {course_counts.index[0]} ({course_counts.iloc[0]} students)")

# 2. Top 3 students by Grade
top3 = df.sort_values("Grade", ascending=False).head(3)
print("\n2) Top 3 students:")
print(top3[["Name", "Course", "Grade"]])

# 3. Average attendance: Pass vs Fail
pass_attendance = df[df["Passed"] == 1]["Attendance"].mean()
fail_attendance = df[df["Passed"] == 0]["Attendance"].mean()
print(f"\n3) Average attendance - Pass: {pass_attendance:.1f}%, Fail: {fail_attendance:.1f}%")

# 4. Correlation between Attendance and Grade
print("\n4) Correlation table:")
print(df[["Attendance", "Grade"]].corr().round(3))
r = df["Attendance"].corr(df["Grade"])
print(f"Correlation Attendance vs Grade: {r:.3f}")
# 0.988 is very close to 1.0 -> a very strong POSITIVE relationship:
# students who attend more get higher grades. (Correlation is not proof of cause,
# and this small, tidy dataset is clearly made up - real data is never this neat.)

# 5. Course summary -> DATA/eda_report.csv
report = df.groupby("Course").agg(
    Student_Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate_Pct=("Passed", "mean"),
    Scholarship_Pct=("Has_Scholarship", "mean"),
)
report["Pass_Rate_Pct"] = report["Pass_Rate_Pct"] * 100
report["Scholarship_Pct"] = report["Scholarship_Pct"] * 100
report = report.round(1)
report = report.reset_index()          # Course back to a normal column

report.to_csv("DATA/eda_report.csv", index=False)
print("\n5) Course summary (saved to DATA/eda_report.csv):")
print(report)
