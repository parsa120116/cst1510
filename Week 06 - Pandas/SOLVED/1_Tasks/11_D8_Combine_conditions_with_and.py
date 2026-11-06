import pandas as pd

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100

warning_rows = df[(df["percent"] >= 90) & (df["percent"] < 100)]
print(warning_rows)

far_rows = df[(df["percent"] < 50) | (df["percent"] > 110)]
print(far_rows)
