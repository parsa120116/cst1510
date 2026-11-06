"""
RECORD CHECK  -  my version
===========================

Name  :  Parsa
Lane  :  IT
Date  :  Week 7 lab

Run it:   python template.py
Data  :   raw_servers.txt  (one messy record per line: hostname, used=..., total=...)
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy raw line and return a dict with clean keys and number values."""
    line = raw_line.strip().lower()             # outer spaces gone, all lowercase
    hostname_part, rest = line.split(",", 1)    # hostname | all the key=value fields

    record = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK for how full a server is."""
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def load_raw_lines(filename):
    """Read a text file and return its non-empty lines, still messy, as a list."""
    raw_lines = []
    with open(filename) as file:
        for line in file:
            if line.strip() != "":
                raw_lines.append(line)
    return raw_lines


# ====================================================================== INPUT
try:
    raw_records = load_raw_lines("raw_servers.txt")
except FileNotFoundError:
    print("raw_servers.txt not found - put it in the same folder as this file.")
    raw_records = []


# =============================================================== PROCESS + OUTPUT
record_count = 0
flagged_count = 0
skipped_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
    except ValueError:
        print(f"{'SKIPPED':<10} Could not parse: {raw_record.strip()}")
        skipped_count += 1
        continue

    status = status_of(record["used"], record["total"])
    print(f"{status:<10} {record}")
    record_count += 1
    if status != "OK":
        flagged_count += 1

print(f"Summary: {record_count} records, {flagged_count} flagged (OVER LIMIT or WARNING), {skipped_count} lines could not be parsed.")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records (8 in raw_servers.txt)
#    [x] Run it with a value that will not convert to a number - the error was:
#        ValueError: could not convert string to float: 'n/a'
#        (now caught: that line is printed as SKIPPED instead of crashing)
#    [x] Check every function does one job, with a docstring
