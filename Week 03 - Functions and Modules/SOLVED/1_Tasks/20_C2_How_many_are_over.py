def count_over(*values, limit=100):
    """Return how many of the values are greater than limit."""
    count = 0
    for value in values:
        if value > limit:
            count += 1
    return count

print(count_over(87, 120, 45, 101))
print(count_over(87, 120, 45, 101, limit=50))
print(count_over())
