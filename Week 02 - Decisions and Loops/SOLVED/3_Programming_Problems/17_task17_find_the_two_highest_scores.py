count = int(input("Enter the number of students: "))

if count < 2:
    print("You need at least two students to find the two highest scores.")
else:
    highest = -1          # scores are 0 or more, so -1 is lower than any real score
    second_highest = -1

    for i in range(count):
        score = float(input(f"Enter the score for student {i + 1}: "))

        if score > highest:
            second_highest = highest   # the old champion moves down to second place
            highest = score
        elif score > second_highest:
            second_highest = score

    print(f"Highest score: {highest}")
    print(f"Second highest score: {second_highest}")
