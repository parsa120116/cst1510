from math import tan, pi


def pentagon_area(side):
    """Return the area of a regular pentagon with the given side length."""
    return 5 * side ** 2 / (4 * tan(pi / 5))


side = float(input("Enter the side length s: "))
print(f"Area = {pentagon_area(side):.2f}")
