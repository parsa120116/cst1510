import math


def mean(values):
    """Return the average of the values."""
    return sum(values) / len(values)


def median(values):
    """Return the middle value (or the average of the two middle values)."""
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def sample_std_dev(values):
    """Return the sample standard deviation (divide by n - 1)."""
    average = mean(values)
    total_squares = 0
    for value in values:
        total_squares += (value - average) ** 2
    return math.sqrt(total_squares / (len(values) - 1))


parts = input("Enter five numbers separated by spaces: ").split()
while len(parts) != 5:
    print("Please enter exactly five numbers.")
    parts = input("Enter five numbers separated by spaces: ").split()

values = []
for part in parts:
    values.append(float(part))

shown = ", ".join(parts)
print(f"Values: {shown}")
print(f"Total = {sum(values):.2f}")
print(f"Mean = {mean(values):.2f}")
print(f"Median = {median(values):.2f}")
print(f"Std Dev = {sample_std_dev(values):.2f}")
