class Dog:
    """A dog with a name and an age."""

    def __init__(self, name, age):
        """Store the dog's name and age."""
        self.name = name
        self.age = age

    def bark(self):
        """Print this dog's bark."""
        print(f"{self.name} says Woof!")

    def birthday(self):
        """Make this dog one year older."""
        self.age += 1


my_dog = Dog("Rex", 3)
my_dog.bark()

print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.birthday()
my_dog.birthday()
print(f"After two birthdays, {my_dog.name} is {my_dog.age} years old.")
