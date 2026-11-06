import math

print("Number      Square root")
for number in range(0, 20, 2):
    print(f"{number:<12}{math.sqrt(number):.2f}")
