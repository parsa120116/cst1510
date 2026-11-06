messy = "***srv-01***"
print(messy.strip("*"))     # remove * from both ends
print(messy.lstrip("*"))    # remove * from the LEFT end only
print(messy.rstrip("*"))    # remove * from the RIGHT end only

field = "  SRV-01  "
print(field.strip().lower())    # first strip, then lower the result
