import random

throws = []
for _ in range(7):
    throws.append(random.randint(1, 6))
print("Throws:", throws)

random.shuffle(throws)
print("Shuffled:", throws)

throws.sort(reverse=True)
print("Sorted (descending):", throws)

print("Occurrences:")
for face in range(1, 7):
    count = throws.count(face)
    if count > 0:
        print(f"{face} appears {count} time(s)")
