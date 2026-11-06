numbers = []

value = int(input("Enter an integer (0 to stop): "))
while value != 0:
    numbers.append(value)
    value = int(input("Enter an integer (0 to stop): "))

print("The values in reverse order:")
for number in numbers[::-1]:
    print(number)
