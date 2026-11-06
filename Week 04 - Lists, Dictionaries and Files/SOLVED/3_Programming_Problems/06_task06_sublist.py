def isSublist(larger, smaller):
    """Return True if smaller appears inside larger as one unbroken piece."""
    if len(smaller) == 0:
        return True
    size = len(smaller)
    for start in range(len(larger) - size + 1):
        if larger[start:start + size] == smaller:
            return True
    return False


big = [1, 2, 3, 4]
tests = [[1], [2, 3], [2, 4], [], [1, 2, 3, 4], [3, 4, 5], [4], [4, 3]]

for small in tests:
    print(f"{small} is a sublist of {big}: {isSublist(big, small)}")
