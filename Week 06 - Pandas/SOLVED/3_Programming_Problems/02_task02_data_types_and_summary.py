import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

print("Data type of each column:")
print(df.dtypes)

print("\nSummary statistics:")
print(df.describe())

average_grade = df["Grade"].mean()
max_attendance = df["Attendance"].max()
youngest_age = df["Age"].min()

print(f"\nThe average grade is {average_grade:.2f}")
print(f"The maximum attendance is {max_attendance}")
print(f"The youngest student is {youngest_age} years old")
