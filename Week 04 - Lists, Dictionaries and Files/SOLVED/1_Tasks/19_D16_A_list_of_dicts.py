records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0},
]

for record in records:
    if record["value"] > record["limit"]:
        status = "OVER LIMIT"
    else:
        status = "OK"
    print(f"{record['label']}: {status}")
