import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})
print(df.dtypes)

df["value"] = df["value"].astype(int)     # turn the text "87" into the number 87
df["percent"] = (df["value"] / df["limit"]) * 100

print(df)
