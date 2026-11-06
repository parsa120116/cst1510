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


record_dict = {"label": "R-001", "value": 87.0}
record_obj = Record("R-001", 87.0, 100.0)

print(record_dict["label"])   # dict: square brackets and the key as a string
print(record_obj.label)       # object: a dot and the attribute name (no quotes)
# A dict can have any keys (or be missing some); every Record object is
# guaranteed to have label, value and limit, because __init__ sets them.
# And an object can also have methods (behaviour), which a dict cannot.
