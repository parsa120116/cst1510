FIELD_NAMES = ["name", "age", "email", "phone"]


def validate_record(record):
    """Return a list of error messages for one CSV record (an empty list means valid)."""
    errors = []
    fields = [field.strip() for field in record.split(",")]

    # 1. Exactly 4 fields
    if len(fields) != 4:
        errors.append(f"Expected 4 fields, found {len(fields)}")
        return errors

    # Every field must be non-empty before we check anything else
    if not all(fields):
        for index in range(len(fields)):
            if fields[index] == "":
                errors.append(f"The {FIELD_NAMES[index]} field is empty")
        return errors

    name, age, email, phone = fields

    # 2. Name: only letters and spaces
    if not name.replace(" ", "").isalpha():
        errors.append(f"Name '{name}' must contain only letters and spaces")

    # 3. Age: a whole number between 18 and 100
    if not age.isdigit():
        errors.append(f"Age '{age}' is not a number")
    elif not 18 <= int(age) <= 100:
        errors.append(f"Age {age} is not between 18 and 100")

    # 4. Email: needs "@" and "."
    if "@" not in email or "." not in email:
        errors.append(f"Email '{email}' must contain '@' and '.'")

    # 5. Phone: starts with "+" or "0"
    if not (phone.startswith("+") or phone.startswith("0")):
        errors.append(f"Phone '{phone}' must start with '+' or '0'")

    return errors


records = [
    "Alice Smith,25,alice@email.com,+447123456789",
    "Bob,abc,bob@email,07123456789",
    "Charlie123,30,charlie@mail.com,447123456789",
    ",22,missing@mail.com,+440000000000"
]

for record in records:
    problems = validate_record(record)
    print(record)
    if len(problems) == 0:
        print("  VALID")
    else:
        for problem in problems:
            print(f"  - {problem}")
