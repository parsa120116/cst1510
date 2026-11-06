import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

df["status"].value_counts().plot(kind="bar")
plt.title("Records per status")
plt.ylabel("Number of records")
plt.tight_layout()          # make room so the long labels are not cut off
plt.savefig("status_counts.png")
plt.show()
