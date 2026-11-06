import platform


def print_banner(hostname):
    """Print the host name, operating system and Python version, one per line."""
    print(f"Host: {hostname}")
    print(f"OS: {platform.system()}")
    print(f"Python: {platform.python_version()}")


hostname = input("Hostname: ").strip()
print_banner(hostname)
