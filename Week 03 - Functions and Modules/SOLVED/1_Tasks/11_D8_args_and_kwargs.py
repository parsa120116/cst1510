def total(*numbers):
    """Return the sum of all the numbers passed in."""
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
print(total())


def configure(**settings):
    """Print each setting as key = value."""
    for key, value in settings.items():
        print(f"{key} = {value}")

configure(host="10.0.0.1", port=8080)
