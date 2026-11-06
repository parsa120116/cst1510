record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record["label"])      # read by key

record["status"] = "OK"     # new key -> added
record["value"] = 90.0      # existing key -> updated

print(record)


print(record.get("status"))
print(record.get("owner"))
print(record.get("owner", "n/a"))


# a) keys only
for key in record:
    print(key)

# b) values only
for value in record.values():
    print(value)

# c) both
for key, value in record.items():
    print(f"{key}: {value}")
