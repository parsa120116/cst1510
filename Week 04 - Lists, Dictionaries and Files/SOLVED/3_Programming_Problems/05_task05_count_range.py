def countRange(data, minimum, maximum):
    """Return how many values are >= minimum and < maximum."""
    count = 0
    for value in data:
        if minimum <= value < maximum:
            count += 1
    return count


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
float_list = [1.5, 2.25, 3.0, 4.75, 5.5, 6.0]
mixed_list = [-5, 0, 5, 10, 15, 20]

print("int_list, 3 to 7:", countRange(int_list, 3, 7))              # 3, 4, 5, 6 -> 4
print("int_list, 1 to 11:", countRange(int_list, 1, 11))            # all -> 10
print("float_list, 2.0 to 5.5:", countRange(float_list, 2.0, 5.5))  # 2.25, 3.0, 4.75 -> 3
print("float_list, 6.0 to 10.0:", countRange(float_list, 6.0, 10.0))  # 6.0 -> 1
print("mixed_list, -10 to 0:", countRange(mixed_list, -10, 0))      # -5 -> 1
print("empty list, 0 to 100:", countRange([], 0, 100))              # -> 0
