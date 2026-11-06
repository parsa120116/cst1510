line = "2026-09-08 ERROR failed login"

print("ERROR" in line)            # exact match, capitals
print("error" in line)            # not found: the line has ERROR, not error
print("error" in line.lower())    # lower the line first, then search
