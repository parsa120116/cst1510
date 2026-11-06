# FIXED: split only at the FIRST "=", so we always get exactly 2 pieces.

piece = "note=server=east"
key, value = piece.split("=", 1)

print(key, value)
