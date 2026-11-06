# FINDINGS (two sentences):
# Category A is the strongest, with an average score of 81.5 on the answered rows
# (B 76.7, C 61.5), and 6 of the 7 real answers are a Pass.
# 3 of the 10 rows (30%) were no-responses and had to be dropped before any averaging.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and look
df = pd.read_csv("survey_results.csv")
print(df.head())
print()
print(df.dtypes)
print(f"\nRows: {len(df)}")

# 2. Measure the gap: what percentage of rows were not answered?
unanswered = df[df["answered"] == 0]
gap_percent = len(unanswered) / len(df) * 100
print(f"\nUnanswered rows: {len(unanswered)} of {len(df)} ({gap_percent:.0f}%)")

# 3. Filter it clean: keep only answered rows (.copy() = a new, independent DataFrame)
clean = df[df["answered"] == 1].copy()
print(f"Rows kept: {len(clean)}")

# 4. Group it: average score per category, on the clean data
category_average = clean.groupby("category")["score"].mean().round(1)
print("\nAverage score per category (clean data):")
print(category_average)

# Why we cleaned first: the same average on the ORIGINAL data
wrong_average = df.groupby("category")["score"].mean().round(1)
print("\nFor comparison, WITHOUT cleaning (the zeros drag it down):")
print(wrong_average)

# 5. Sort it: which category is strongest?
ranked = category_average.sort_values(ascending=False)
print(f"\nStrongest category: {ranked.index[0]} (average {ranked.iloc[0]})")

# 6. Classify it: Pass / Fail with apply + lambda
clean["result"] = clean["score"].apply(lambda s: "Pass" if s >= 60 else "Fail")
print()
print(clean)
print()
print(clean["result"].value_counts())

# 7. Chart it: pass/fail counts
clean["result"].value_counts().plot(kind="bar")
plt.title("Survey results (answered only)")
plt.xlabel("Result")
plt.ylabel("Number of students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survey_pass_fail.png")
print("\nSaved survey_pass_fail.png")
plt.show()

# 8. Save it: the cleaned, classified DataFrame
clean.to_csv("survey_results_clean.csv", index=False)
print("Saved survey_results_clean.csv")
