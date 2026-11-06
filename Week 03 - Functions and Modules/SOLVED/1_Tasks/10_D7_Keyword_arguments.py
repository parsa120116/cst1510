def status_of(percent, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95))
print(status_of(85))
print(status_of(85, 80))


print(status_of(percent=95, warning_at=96))
print(status_of(warning_at=96, percent=95))
print(status_of(95, warning_at=96))
