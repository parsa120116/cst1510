people = []      # a list of (name, age) tuples

with open("DATA/ages.csv", encoding="utf-8-sig") as file:
    file.readline()                     # skip the header "name,age"
    for line in file:
        line = line.strip()
        if line == "":
            continue
        name, age = line.split(",")
        people.append((name, int(age)))

print("People:", people)

oldest = people[0]
youngest = people[0]
total_age = 0
for person in people:
    if person[1] > oldest[1]:
        oldest = person
    if person[1] < youngest[1]:
        youngest = person
    total_age += person[1]

average_age = total_age / len(people)
print(f"Oldest: {oldest[0]} ({oldest[1]})")
print(f"Youngest: {youngest[0]} ({youngest[1]})")
print(f"Average age: {average_age:.2f}")

with open("adults.txt", "w") as out_file:
    for name, age in people:
        if age > 20:
            out_file.write(f"{name}: {age}\n")

with open("adults.txt") as check_file:
    print("adults.txt contains:")
    print(check_file.read())
