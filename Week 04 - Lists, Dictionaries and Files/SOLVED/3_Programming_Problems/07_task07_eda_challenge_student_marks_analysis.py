student_data = [
    [101, 'Alice', 85, 92, 88],
    [102, 'Bob', 78, 81, 75],
    [103, 'Charlie', 90, 85, 89],
    [104, 'David', 65, 70, 72],
    [105, 'Eve', 88, 95, 90]
]


def get_average(student):
    """Return the average of a student's three subject scores."""
    return (student[2] + student[3] + student[4]) / 3


# 1. Add each student's average as a new element at the end of their list
for student in student_data:
    student.append(round(get_average(student), 2))

print("Data with averages:")
for student in student_data:
    print(student)

# 2. Highest and lowest averages
averages = [student[5] for student in student_data]
highest = max(averages)
lowest = min(averages)

for student in student_data:
    if student[5] == highest:
        print(f"Highest average: {highest} ({student[1]})")
    if student[5] == lowest:
        print(f"Lowest average: {lowest} ({student[1]})")

# 3. Students who scored above 75 in all three subjects
top_students = [student[1] for student in student_data
                if student[2] > 75 and student[3] > 75 and student[4] > 75]
print("Above 75 in all subjects:", top_students)
