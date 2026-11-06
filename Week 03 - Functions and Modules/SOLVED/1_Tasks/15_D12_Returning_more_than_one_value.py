def check_record(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

difference, percent = check_record(87.0, 100.0)
print("Difference:", difference)
print("Percent:", percent)
