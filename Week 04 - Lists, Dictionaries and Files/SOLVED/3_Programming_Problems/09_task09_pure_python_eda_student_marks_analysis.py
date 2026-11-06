marks = [72, 45, 88, 50, 39, 91, 64, 58, 47, 80]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print(f"Marks: {marks}")
print(f"Average mark: {average:.2f}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
