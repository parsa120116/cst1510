def sum_row(matrix, rowIndex):
    """Return the sum of all the elements in one row of the matrix."""
    total = 0
    for value in matrix[rowIndex]:
        total += value
    return total


matrix = []
print("Enter a 4-by-4 matrix row by row (4 numbers per line, separated by spaces):")
for row in range(4):
    line = input(f"Row {row}: ")
    numbers = [float(item) for item in line.split()]
    matrix.append(numbers)

for row in range(4):
    print(f"Sum of the elements in row {row} is {sum_row(matrix, row)}")
