count = int(input("Enter the number of students: "))

best_name = ""
best_score = 0

for i in range(count):
    name = input(f"Enter student {i + 1} name: ")
    score = float(input(f"Enter {name}'s score: "))

    # The first student is the best so far; after that, only a higher score wins
    if i == 0 or score > best_score:
        best_name = name
        best_score = score

if count > 0:
    print(f"The top student is {best_name} with a score of {best_score}")
else:
    print("No students were entered.")
