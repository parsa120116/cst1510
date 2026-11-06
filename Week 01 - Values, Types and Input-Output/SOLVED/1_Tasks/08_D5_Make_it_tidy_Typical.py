record_id = input("Record ID: ")
value = float(input("Value: "))
limit = float(input("Limit: "))

difference = value - limit
percent = value / limit * 100

print(f"Record ID  : {record_id}")
print(f"Value      : {value:>10.2f}")
print(f"Limit      : {limit:>10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percent    : {percent:>10.2f} %")
