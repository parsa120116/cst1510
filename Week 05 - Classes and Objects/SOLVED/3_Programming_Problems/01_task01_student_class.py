class Student:
    """A student with a name and an age."""

    def __init__(self, name, age):
        """Store the name and age on the new object."""
        self.name = name
        self.age = age


student1 = Student("Alice", 19)
student2 = Student("Parsa", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)

print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")
