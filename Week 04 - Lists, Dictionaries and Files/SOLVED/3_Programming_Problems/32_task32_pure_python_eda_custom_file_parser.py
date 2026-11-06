def parse_csv_to_dicts(filepath):
    """Read a comma-separated file and return a list of dicts, one per row."""
    rows = []
    with open(filepath, encoding="utf-8-sig") as file:
        header = file.readline().strip().split(",")
        for line in file:
            line = line.strip()
            if line == "":
                continue                       # skip empty lines
            values = line.split(",")
            row = {}
            for index in range(len(header)):
                row[header[index]] = values[index]
            rows.append(row)
    return rows


people = parse_csv_to_dicts("DATA/sample_data.csv")

print("Rows read:", len(people))
print("Columns:", list(people[0].keys()))
print("First row:", people[0])

# 1. Average age (the values are text, so convert with int)
ages = [int(person["Age"]) for person in people]
print(f"Average age: {sum(ages) / len(ages):.1f}")

# 2. Oldest and youngest person
oldest = people[0]
youngest = people[0]
for person in people:
    if int(person["Age"]) > int(oldest["Age"]):
        oldest = person
    if int(person["Age"]) < int(youngest["Age"]):
        youngest = person
print(f"Oldest: {oldest['Name']} ({oldest['Age']}, {oldest['City']})")
print(f"Youngest: {youngest['Name']} ({youngest['Age']}, {youngest['City']})")

# 3. Filter: people older than 30
over_30 = [person["Name"] for person in people if int(person["Age"]) > 30]
print("Older than 30:", over_30)

# 4. Count people per country
per_country = {}
for person in people:
    country = person["Country"]
    per_country[country] = per_country.get(country, 0) + 1
print("People per country:", per_country)

# The same function works on another CSV file too
print("ages.csv:", parse_csv_to_dicts("DATA/ages.csv"))
