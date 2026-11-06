import pandas as pd

df = pd.read_csv("DATA/students.csv")

bins = [0, 59, 69, 79, 89, 100]
labels = ["F", "D", "C", "B", "A"]
df["Grade_Band"] = pd.cut(df["Grade"], bins=bins, labels=labels)

print(df[["Name", "Grade", "Grade_Band"]].head(10))

print("\nStudents per Grade Band:")
print(df["Grade_Band"].value_counts().sort_index(ascending=False))

top_bands = df[df["Grade_Band"].isin(["A", "B"])]
print("\nA or B students per course:")
print(top_bands["Course"].value_counts())
