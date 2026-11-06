class Student:
    """A student with a name and an age."""

    def __init__(self, name, age):
        """Store the name and age on the new object."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return how this student looks when printed."""
        return f"{self.name} (age {self.age})"


students = [
    Student("Alice", 19),
    Student("Parsa", 20),
    Student("Sara", 22),
    Student("Reza", 18),
    Student("Mina", 21),
]

for student in students:
    print(student)

# __str__ is also used by str() and inside f-strings
first = students[0]
print("First on the list: " + str(first))
print(f"Last on the list: {students[-1]}")
