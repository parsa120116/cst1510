# FINDINGS (two sentences):
# north has the highest average usage (88.7%), ahead of west (81.0%) and east (71.8%),
# and 5 of the 10 servers are at or above 90%.
# srv-03 (west) is the single most at-risk server at 120%, and 3 servers are already OVER LIMIT.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and look
df = pd.read_csv("servers.csv")
print(df.head())
print()
print(df.dtypes)
print()
print(f"Servers (rows): {len(df)}")
print(f"Columns: {len(df.columns)} -> {df.columns.tolist()}")

# 2. Add a column - whole-column arithmetic, no loop
df["percent"] = (df["used"] / df["total"]) * 100

# 3. A question with a filter: how many servers are at or above 90%?
high_usage = df[df["percent"] >= 90]
print(f"\nServers at or above 90%: {len(high_usage)}")
print(high_usage[["hostname", "region", "percent"]])

# 4. A question with a group: average percent per region
region_average = df.groupby("region")["percent"].mean().round(1)
print("\nAverage percent per region (highest first):")
print(region_average.sort_values(ascending=False))

# 5. Sort it: the single most at-risk server
ranked = df.sort_values("percent", ascending=False)
most_at_risk = ranked.iloc[0]
print(f"\nMost at risk: {most_at_risk['hostname']} ({most_at_risk['region']}) "
      f"at {most_at_risk['percent']:.0f}%")

# 6. Classify it: status column with apply + lambda (same thresholds as the walkthrough)
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print()
print(df)
print()
print(df["status"].value_counts())

# 7. Chart it: servers per status
status_counts = df["status"].value_counts()
status_counts.plot(kind="bar")
plt.title("Servers per status")
plt.xlabel("Status")
plt.ylabel("Number of servers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("servers_per_status.png")
print("\nSaved servers_per_status.png")
plt.show()

# 8. Save it: only the OVER LIMIT rows
at_risk = df[df["status"] == "OVER LIMIT"]
at_risk.to_csv("servers_at_risk.csv", index=False)
print(f"Saved servers_at_risk.csv ({len(at_risk)} rows)")
