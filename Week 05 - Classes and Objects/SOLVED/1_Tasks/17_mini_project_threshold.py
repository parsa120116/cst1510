class Record:
    """One server record: hostname, GB used and GB total."""

    def __init__(self, label, value, limit):
        """Store the three fields as attributes."""
        self.label = label
        self.value = value
        self.limit = limit


records = [
    Record("srv-01", 87.0, 120.0),
    Record("srv-02", 125.0, 120.0),
]

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used        : {record.value:>10.2f}")
    print(f"  Total       : {record.limit:>10.2f}")
    print("=" * 34)
