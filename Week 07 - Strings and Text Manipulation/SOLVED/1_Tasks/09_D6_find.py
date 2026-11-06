# Each block runs on its own, so we create line again.
line = "2026-09-08 ERROR failed login"

print(line.find("ERROR"))      # the index where ERROR starts
print(line.find("WARNING"))    # -1 means not found
