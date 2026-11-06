import pandas as pd

df = pd.read_csv("DATA/students.csv")

course_stats = df.groupby("Course").agg(
    Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Max_Grade=("Grade", "max"),
    Avg_Attendance=("Attendance", "mean"),
)

# Round the two averages to 1 decimal place
course_stats["Avg_Grade"] = course_stats["Avg_Grade"].round(1)
course_stats["Avg_Attendance"] = course_stats["Avg_Attendance"].round(1)

# Highest average grade first
course_stats = course_stats.sort_values("Avg_Grade", ascending=False)
print(course_stats)
