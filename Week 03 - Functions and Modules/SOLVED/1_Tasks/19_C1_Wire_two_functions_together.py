def percent_of(part, total):
    """Return part as a percentage of total."""
    return (part / total) * 100

def status_of(percent, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(percent_of(87, 100)))
print(status_of(percent_of(120, 100)))
print(status_of(percent_of(45, 100)))
