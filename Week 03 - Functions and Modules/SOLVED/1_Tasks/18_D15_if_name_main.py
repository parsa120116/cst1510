import math

print(__name__)

def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    print(round(area_of_circle(5), 2))
    # This would NOT run if another file imported this one
    # (import my_file): then __name__ is "my_file", not "__main__".
