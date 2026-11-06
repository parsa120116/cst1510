raw_line = "  Srv-01 , used=87 , total=100  "

# 1. strip the whole line
line = raw_line.strip()

# 2. split off the hostname (cut at the FIRST comma only)
hostname_part, rest = line.split(",", 1)

# 3. clean the hostname
hostname = hostname_part.strip().lower()

# 4 + 5. split the rest into key=value pieces and build one dict
record = {"hostname": hostname}
for piece in rest.split(","):
    key, value = piece.split("=")
    record[key.strip()] = float(value.strip())

print(record)
