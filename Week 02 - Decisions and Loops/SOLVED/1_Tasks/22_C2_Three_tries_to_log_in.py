correct_password = "python123"
max_tries = 3
tries = 0
granted = False

while tries < max_tries:
    attempt = input("Password: ")
    tries += 1
    if attempt == correct_password:
        granted = True
        break
    print(f"Wrong password ({tries} of {max_tries})")

if granted:
    print(f"Access granted (after {tries} tries)")
else:
    print("Account locked")
