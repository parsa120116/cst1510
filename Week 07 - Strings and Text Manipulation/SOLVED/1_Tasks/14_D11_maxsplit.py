record = "srv-01,used=87,total=100"

print(record.split(","))       # cut at EVERY comma
print(record.split(",", 1))    # cut at the FIRST comma only (maxsplit=1)
