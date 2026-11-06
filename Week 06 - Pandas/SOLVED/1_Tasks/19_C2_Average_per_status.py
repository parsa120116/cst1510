import pandas as pd

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

average_per_status = df.groupby("status")["percent"].mean().round(1)
print(average_per_status)
