class Record:
    """One record: a label, a value and its limit."""

    def __init__(self, label, value, limit):
        """Store the three fields on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def is_over(self):
        """Return True if the value is over the limit."""
        return self.value > self.limit


def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("records_sample.txt")
over = 0
for record in records:
    if record.is_over():
        over += 1
print(f"{over} of {len(records)} records are OVER LIMIT")
