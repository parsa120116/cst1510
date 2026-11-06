with open("servers.txt", "w") as f:
    f.write("srv-01,87,120\nsrv-02,125,120\nsrv-03,110,120\nsrv-04,40,120\n")
print("servers.txt ready")

"""
RECORD CHECK  -  my version
Name  : Parsa
Lane  : IT
Run it:   python template.py
Data  :   servers.txt  (one record per line: hostname,GB used,GB total)
"""

# ===================================================================== CLASS
class Record:
    """One server record: hostname, GB used and GB total."""

    def __init__(self, label, value, limit):
        """Store the three fields as attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the space used as a percentage of the total."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


# =================================================================== RECORDS
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("servers.txt")

# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()                 # call once, keep the result
    if status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used        : {record.value:>10.2f}")
    print(f"  Total       : {record.limit:>10.2f}")
    print(f"  Percent     : {record.percent():>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print(f"\n{over_limit_count} of {len(records)} record(s) OVER LIMIT.")
