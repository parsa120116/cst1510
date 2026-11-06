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


print(parse_line("SRV-02,used=120,total=100"))
