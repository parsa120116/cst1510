import statistics as stats


def read_five_numbers():
    """Ask until the user types exactly five numbers; return the typed pieces."""
    while True:
        parts = input("Enter five numbers separated by spaces: ").split()
        if len(parts) == 5:
            return parts
        print("Please enter exactly five numbers.")


parts = read_five_numbers()
values = []
for part in parts:
    values.append(float(part))

shown = ", ".join(parts)
print(f"Values: {shown}")
print(f"Total = {sum(values):.2f}")
print(f"Mean = {stats.mean(values):.2f}")
print(f"Median = {stats.median(values):.2f}")
print(f"Std Dev = {stats.stdev(values):.2f}")
