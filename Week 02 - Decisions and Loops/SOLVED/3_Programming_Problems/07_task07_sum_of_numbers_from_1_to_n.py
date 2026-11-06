n = int(input("Enter the value n: "))

total = 0
for number in range(1, n + 1):
    total += number

print(f"The sum of all numbers until {n} is {total}")
