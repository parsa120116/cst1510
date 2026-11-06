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


def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


with open("messy_lines.txt") as file:
    for raw_line in file:
        if raw_line.strip() == "":
            continue                        # skip empty lines
        record = parse_line(raw_line)
        status = status_of(record["used"], record["total"])
        print(record["hostname"], status)
