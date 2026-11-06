import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

# 1. Overall average grade (the line every city is compared with)
overall_mean = df["Grade"].mean()
print(f"Overall average grade: {overall_mean:.2f}\n")

# 2. Basic summary per city
city_report = df.groupby("City").agg(
    Students=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
)

# 3. Pass rate inside each city group (% with Grade >= 60)
city_pass = df.groupby("City")["Grade"].apply(
    lambda grades: (grades >= 60).sum() / len(grades) * 100
)
city_report["Pass_Rate"] = city_pass

# 4. Above / below the overall mean (compare BEFORE rounding)
city_report["Performance"] = city_report["Avg_Grade"].apply(
    lambda avg: "Above Average" if avg > overall_mean else "Below Average"
)

# Round the numbers to 1 decimal place
city_report["Avg_Grade"] = city_report["Avg_Grade"].round(1)
city_report["Avg_Attendance"] = city_report["Avg_Attendance"].round(1)
city_report["Pass_Rate"] = city_report["Pass_Rate"].round(1)

# City is the index -> make it a normal column, so index=False does not lose it
city_report = city_report.reset_index()

# 6. Highest average grade first
city_report = city_report.sort_values("Avg_Grade", ascending=False)

# 5. Save without the index
city_report.to_csv("DATA/city_report.csv", index=False)

print(city_report)
print("\nSaved DATA/city_report.csv")
