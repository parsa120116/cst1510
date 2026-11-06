import pandas as pd

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100

print(df["label"])
print(df[["label", "percent"]])
