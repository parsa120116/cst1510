import pandas as pd

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100

df["over"] = df["percent"] >= 100

summary = df.groupby("over")["percent"].agg(["mean", "max", "min"])
print(summary)

print(df["over"].value_counts())
