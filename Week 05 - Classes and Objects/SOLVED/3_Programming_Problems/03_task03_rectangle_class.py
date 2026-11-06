class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Store the width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of this rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of this rectangle."""
        return 2 * (self.width + self.height)


rectangles = [
    Rectangle(3, 4),
    Rectangle(5, 2),
    Rectangle(6, 6),
    Rectangle(2, 8),
]

for number, rectangle in enumerate(rectangles, start=1):
    print(f"Rectangle {number}: {rectangle.width} x {rectangle.height} "
          f"-> area {rectangle.area()}, perimeter {rectangle.perimeter()}")

# Find the largest area (the "best so far" pattern)
largest = rectangles[0]
largest_number = 1
for number, rectangle in enumerate(rectangles, start=1):
    if rectangle.area() > largest.area():
        largest = rectangle
        largest_number = number

print(f"Largest: Rectangle {largest_number} ({largest.width} x {largest.height}) "
      f"with area {largest.area()}")
