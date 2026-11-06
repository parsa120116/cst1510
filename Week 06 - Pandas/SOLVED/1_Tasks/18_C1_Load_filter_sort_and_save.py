import pandas as pd

# Load
df = pd.read_csv("records_sample.csv")

# Add percent and status
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# Filter, then sort
over_limit = df[df["status"] == "OVER LIMIT"]
over_limit = over_limit.sort_values("percent", ascending=False)

# Save and print
over_limit.to_csv("over_limit.csv", index=False)
print(over_limit)
