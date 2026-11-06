raw_names = [
    "  JOHN smith  ",
    "mary JOHNSON",
    "  bob WILSON  "
]

for raw_name in raw_names:
    clean_name = raw_name.strip().title()
    first_name, surname = clean_name.split()
    email = first_name.lower() + "." + surname.lower() + "@company.com"
    print(f"{clean_name} → {email}")
