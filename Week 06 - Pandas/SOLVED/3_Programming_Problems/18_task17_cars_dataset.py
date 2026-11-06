import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/CARS.text")
print(f"Loaded {len(df)} cars, columns: {df.columns.tolist()}")

# 1. Best and worst mpg
columns = ["model", "mpg", "cyl", "hp", "wt", "am"]
print("\n5 cars with the best mpg:")
print(df.sort_values("mpg", ascending=False)[columns].head(5))
print("\n5 cars with the worst mpg:")
print(df.sort_values("mpg", ascending=True)[columns].head(5))

# 2. 4 cylinders AND more than 90 hp
four_cyl_powerful = df[(df["cyl"] == 4) & (df["hp"] > 90)]
print(f"\n4-cylinder cars with hp above 90: {len(four_cyl_powerful)}")
print(four_cyl_powerful[["model", "cyl", "hp", "mpg"]])

# 3. Per number of cylinders: count, average mpg, average hp
cyl_stats = df.groupby("cyl").agg(
    Count=("model", "count"),
    Avg_mpg=("mpg", "mean"),
    Avg_hp=("hp", "mean"),
).round(1)
print("\nBy number of cylinders:")
print(cyl_stats)

# 4. Efficiency category with apply + lambda
df["Efficiency"] = df["mpg"].apply(
    lambda m: "High" if m >= 25 else "Medium" if m >= 18 else "Low"
)
print("\nCars per Efficiency category:")
print(df["Efficiency"].value_counts())

# 5. Save (in the current folder, as the task says)
df.to_csv("cars_clean.csv", index=False)
print("\nSaved cars_clean.csv")
