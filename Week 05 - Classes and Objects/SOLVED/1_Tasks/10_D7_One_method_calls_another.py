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

r = Record("R-001", 87.0, 100.0)
print(r.percent())
print(r.status())
