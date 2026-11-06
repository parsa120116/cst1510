grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Add a new student
grades["Diana"] = 88

# Update Bob's score
grades["Bob"] = 95

print("All grades:", grades)

# Students with scores above 80
print("Students with scores above 80:")
for name, score in grades.items():
    if score > 80:
        print(f"{name}: {score}")

# Average score
average = sum(grades.values()) / len(grades)
print(f"Average score: {average}")
