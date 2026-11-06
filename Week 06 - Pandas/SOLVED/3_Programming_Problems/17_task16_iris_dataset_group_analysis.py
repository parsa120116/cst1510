import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv("DATA/iris_dataset.csv")

# 1. Mean of every measurement per species
species_means = df.groupby("target").mean()
print("Mean per species:")
print(species_means.round(3))

# 2. Largest average petal length / smallest average sepal width
longest_petals = species_means["petal length (cm)"].idxmax()
narrowest_sepals = species_means["sepal width (cm)"].idxmin()
print(f"\nLargest average petal length: {longest_petals} "
      f"({species_means['petal length (cm)'].max():.3f} cm)")
print(f"Smallest average sepal width: {narrowest_sepals} "
      f"({species_means['sepal width (cm)'].min():.3f} cm)")

# 3. New column: petal area, and the 5 largest
df["petal_area"] = df["petal length (cm)"] * df["petal width (cm)"]
print("\n5 flowers with the largest petal area:")
print(df.sort_values("petal_area", ascending=False).head(5))

# 4. Correlation between petal length and petal width
r = df["petal length (cm)"].corr(df["petal width (cm)"])
print(f"\nCorrelation petal length vs petal width: {r:.3f}")
# 0.963 is very close to 1.0 -> a very strong positive relationship:
# flowers with longer petals almost always have wider petals too.
