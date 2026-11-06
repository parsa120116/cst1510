record_id = input("Record ID: ")
value = float(input("Value: "))
limit = float(input("Limit: "))

difference = value - limit
percent = value / limit * 100

print("Record ID:", record_id)
print("Value:", value)
print("Limit:", limit)
print("Difference:", difference)
print("Percent of limit:", percent)
