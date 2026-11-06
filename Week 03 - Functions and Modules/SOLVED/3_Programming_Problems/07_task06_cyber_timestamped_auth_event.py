from datetime import datetime


def make_event_line(username, action):
    """Return a log line like [2025-09-17 14:20:15] LOGIN user=alice."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {action.upper()} user={username}"


username = input("Username: ").strip()
action = input("Action (LOGIN or LOGOUT): ").strip()
print(make_event_line(username, action))
