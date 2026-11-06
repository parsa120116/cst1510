class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r1 = Record("R-001", 87.0, 100.0)
print(r1.label, r1.value, r1.limit)


r2 = Record("R-002", 120.0, 100.0)

r1.value = 95.0

print(r1.value, r2.value)
