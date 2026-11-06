FIELD_NAMES = ["name", "age", "email", "country"]


def clean_dataset(records):
    """Clean and validate |-separated records; return (valid_records, invalid_records)."""
    valid_records = []
    invalid_records = []

    for record in records:
        fields = [field.strip() for field in record.split("|")]

        if len(fields) != 4:
            invalid_records.append({"record": record.strip(),
                                    "reasons": [f"expected 4 fields, found {len(fields)}"]})
            continue

        # 1. Skip records with any empty field
        if not all(fields):
            reasons = []
            for index in range(4):
                if fields[index] == "":
                    reasons.append(f"{FIELD_NAMES[index]} is empty")
            invalid_records.append({"record": record.strip(), "reasons": reasons})
            continue

        name, age, email, country = fields
        reasons = []

        # 2. Name: Title Case, and only one space between words
        name = " ".join(name.split()).title()

        # 3. Age: a number from 18 to 120
        if not age.isdigit():
            reasons.append(f"age '{age}' is not a number")
        elif not 18 <= int(age) <= 120:
            reasons.append(f"age {age} is not between 18 and 120")

        # 4. Email: an "@" and then a "." somewhere after it
        at_position = email.find("@")
        if at_position == -1 or email.find(".", at_position) == -1:
            reasons.append(f"email '{email}' is not valid")

        # 5. Country in uppercase
        country = country.upper()

        if len(reasons) == 0:
            valid_records.append({"name": name, "age": int(age),
                                  "email": email, "country": country})
        else:
            invalid_records.append({"record": record.strip(), "reasons": reasons})

    return valid_records, invalid_records


raw_data = [
    "  john SMITH  | 25 | john.smith@email.com | united kingdom ",
    "  MARY  johnson | abc | mary@email | france",
    " | 30 | test@test.com | germany",
    "  bob wilson  | 17 | bob@mail.com | spain  ",
    "  alice Brown  | 28 | alice.b@data.org | italy  ",
    "charlie DAVIS | 35 | | usa"
]

valid, invalid = clean_dataset(raw_data)

print(f"VALID RECORDS ({len(valid)})")
for person in valid:
    print(f"  {person['name']:<14} {person['age']:>3}  {person['email']:<22} {person['country']}")

print()
print(f"INVALID RECORDS ({len(invalid)})")
for item in invalid:
    print(f"  {item['record']}")
    print(f"     reason: {'; '.join(item['reasons'])}")
