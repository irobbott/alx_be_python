import math

class Shape:
    """A base class to represent a generic shape."""

    def area(self):
        """Raise an error, indicating that subclasses should override this method."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """A class to represent a rectangle."""

    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A class to represent a circle."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2
