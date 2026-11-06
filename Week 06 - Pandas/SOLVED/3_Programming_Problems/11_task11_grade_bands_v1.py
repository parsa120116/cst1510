import pandas as pd

df = pd.read_csv("DATA/students.csv")


def grade_band(grade):
    """Return the letter band (A-F) for a grade."""
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


# 1. New column with apply() + our function (no brackets after grade_band!)
df["Grade_Band"] = df["Grade"].apply(grade_band)

# 2. All students
print(df[["Name", "Grade", "Grade_Band"]])

# 3. Students per band, in A-F order
print("\nStudents per Grade Band:")
print(df["Grade_Band"].value_counts().sort_index())

# 4. Which course has the most A or B students?
top_bands = df[df["Grade_Band"].isin(["A", "B"])]
ab_per_course = top_bands["Course"].value_counts()
print("\nA or B students per course:")
print(ab_per_course)
print(f"Most A/B students: {ab_per_course.index[0]} ({ab_per_course.iloc[0]})")
