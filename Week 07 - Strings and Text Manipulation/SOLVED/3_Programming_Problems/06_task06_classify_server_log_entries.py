def classify_logs(logs):
    """Print each entry's timestamp and return the ERROR, INFO and WARNING counts."""
    error_count = 0
    info_count = 0
    warning_count = 0

    for entry in logs:
        # "[14:32:05] ERROR: Disk full" -> "[14:32:05" and " ERROR: Disk full"
        timestamp_part, message = entry.split("]", 1)
        timestamp = timestamp_part.strip("[")
        message = message.strip()

        if message.startswith("ERROR"):
            error_count += 1
        elif message.startswith("INFO"):
            info_count += 1
        elif message.startswith("WARNING"):
            warning_count += 1

        print(f"Timestamp: {timestamp}  |  {message}")

    return error_count, info_count, warning_count


logs = [
    "[14:32:05] ERROR: Disk full",
    "[14:32:10] INFO: Server started",
    "[14:33:01] WARNING: High memory usage",
    "[14:33:15] INFO: Backup complete",
    "[14:34:00] ERROR: Connection refused",
    "[14:35:22] WARNING: CPU at 90%"
]

error_total, info_total, warning_total = classify_logs(logs)
print()
print(f"ERROR: {error_total}   INFO: {info_total}   WARNING: {warning_total}")
