def get_mean(data):
    """Return the average of a list of numbers."""
    return sum(data) / len(data)


def get_median(data):
    """Return the middle value of a list with an odd number of items."""
    sorted_data = sorted(data)
    middle = len(sorted_data) // 2
    return sorted_data[middle]


regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]

print(f"Regular data: mean = {get_mean(regular_data)}, median = {get_median(regular_data)}")
print(f"Outlier data: mean = {get_mean(outlier_data)}, median = {get_median(outlier_data)}")
