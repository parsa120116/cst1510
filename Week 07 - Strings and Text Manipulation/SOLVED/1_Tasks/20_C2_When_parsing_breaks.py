def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    record = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


lines = ["srv-07,used=50,total=100",
         "srv-08,used=unknown,total=100",
         "srv-09,note=a=b,used=1,total=2"]

for line in lines:
    try:
        print(parse_line(line))
    except ValueError:
        print("Could not parse:", line)
