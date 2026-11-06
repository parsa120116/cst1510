import pandas as pd

# 1. Load both files
excel_df = pd.read_excel("DATA/data.xlsx")
csv_df = pd.read_csv("DATA/sample_data.csv")
print("From data.xlsx:")
print(excel_df)
print("\nFrom sample_data.csv:")
print(csv_df)

# 2. Compare them
same_columns = excel_df.columns.tolist() == csv_df.columns.tolist()
same_shape = excel_df.shape == csv_df.shape
same_everything = excel_df.equals(csv_df)
print(f"\nSame columns: {same_columns}")
print(f"Same shape:   {same_shape} {excel_df.shape}")
print(f"Same rows (identical data): {same_everything}")

# 3. Stack them, then remove duplicate rows
combined = pd.concat([excel_df, csv_df], ignore_index=True)
print(f"\nAfter concat: {len(combined)} rows")
combined = combined.drop_duplicates(ignore_index=True)
print(f"After drop_duplicates: {len(combined)} rows")
print(combined)

# 4. People older than 30, youngest first
older = combined[combined["Age"] > 30].sort_values("Age")
print("\nOlder than 30, sorted by Age:")
print(older)
