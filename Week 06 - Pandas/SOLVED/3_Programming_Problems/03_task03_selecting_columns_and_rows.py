import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/students.csv")

# 1. Only three columns -> a new DataFrame (note the DOUBLE brackets)
grades_df = df[["Name", "Course", "Grade"]]
print("grades_df, first 8 rows:")
print(grades_df.head(8))

# 2. iloc = by POSITION. Rows 5 to 9 -> 5:10 (the end number is NOT included)
print("\nRows at positions 5 to 9 (iloc[5:10]):")
print(df.iloc[5:10])

# 3. loc = by LABEL. Row with index label 3, columns Name and City
print("\nName and City of the student at index 3:")
print(df.loc[3, ["Name", "City"]])

name = df.loc[3, "Name"]
city = df.loc[3, "City"]
print(f"\nIndex 3 is {name}, from {city}.")
