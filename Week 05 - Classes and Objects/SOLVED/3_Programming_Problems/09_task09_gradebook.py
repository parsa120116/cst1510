class Student:
    """A student with a name and a list of marks."""

    def __init__(self, name, marks):
        """Store the name and the list of marks."""
        self.name = name
        self.marks = marks

    def average(self):
        """Return the average of this student's marks (0 if there are none)."""
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        """Return the student's name and average."""
        return f"{self.name}: {self.average():.1f}"


class Course:
    """A course that holds a list of Student objects."""

    def __init__(self, name):
        """Store the course name and start with no students."""
        self.name = name
        self.students = []

    def add_student(self, student):
        """Add one Student object to this course."""
        self.students.append(student)

    def average_mark(self, student_name):
        """Return the average for the named student, or None if not found."""
        for student in self.students:
            if student.name == student_name:
                return student.average()
        return None

    def top_student(self):
        """Return the Student with the highest average (None if empty)."""
        if len(self.students) == 0:
            return None
        best = self.students[0]
        for student in self.students:
            if student.average() > best.average():
                best = student
        return best


course = Course("CST1510 Programming")
course.add_student(Student("Ali", [65, 70, 80]))
course.add_student(Student("Sara", [90, 85, 92]))
course.add_student(Student("Reza", [55, 60, 58]))
course.add_student(Student("Mina", [78, 88, 84]))

print(f"Course: {course.name}")
for student in course.students:
    print(f"  {student.name}: marks {student.marks}, average {course.average_mark(student.name):.1f}")

top = course.top_student()
print(f"Top student: {top.name} with an average of {top.average():.1f}")

# Looking up a name that is not on the course
result = course.average_mark("Bob")
if result is None:
    print("Bob is not on this course.")
