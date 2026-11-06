import pandas as pd

data = {
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
    "limit": [100, 100, 100],
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
