numbers = [87, 100]

# Step 1: this line crashes, so it is left as a comment:
# print(",".join(numbers))
# TypeError: sequence item 0: expected str instance, int found

print(",".join(str(n) for n in numbers))    # turn each number into text first

hostname = "srv-01"
used = 87
total = 100
print(f"{hostname}: {used}/{total} ({used / total * 100:.1f}%)")
