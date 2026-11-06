class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        """Return a short text summary of this record."""
        return f"{self.label}: {self.value}/{self.limit}"

    def status(self):
        """Return OVER LIMIT, WARNING or OK for this record."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

r1 = Record("R-001", 87.0, 100.0)
r2 = Record("R-002", 120.0, 100.0)
r3 = Record("R-003", 95.0, 100.0)
print(r1.status())
print(r2.status())
print(r3.status())
