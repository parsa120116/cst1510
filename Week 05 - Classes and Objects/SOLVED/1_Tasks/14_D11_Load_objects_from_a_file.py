class Record:
    """One record: a label, a value and its limit."""

    def __init__(self, label, value, limit):
        """Store the three fields on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the value as a percentage of the limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK for this record."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 45.0, 100.0),
]

for record in records:
    print(record.label, record.status())


class Counted:
    count = 0                    # class attribute: ONE value shared by the class

    def __init__(self):
        Counted.count += 1       # change the shared value through the class name

a = Counted()
b = Counted()
c = Counted()
print(Counted.count)
# The count is shared because it belongs to the CLASS, not to each object.
# There is only one Counted.count; every new object adds 1 to that same number.


def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("records_sample.txt")
for record in records:
    print(record.label, record.status())
