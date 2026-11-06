import pandas as pd

df = pd.read_csv("records_sample.csv")

print(df.iloc[0]["label"])     # by position: the first row
print(df.loc[2, "value"])      # by label: the row whose index is 2
