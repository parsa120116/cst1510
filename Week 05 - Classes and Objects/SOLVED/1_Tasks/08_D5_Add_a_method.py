class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        """Return a short text summary of this record."""
        return f"{self.label}: {self.value}/{self.limit}"

r = Record("R-001", 87.0, 100.0)
print(r.summary())
