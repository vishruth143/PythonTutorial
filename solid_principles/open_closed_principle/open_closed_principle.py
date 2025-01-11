# Function to calculate areas of different shapes
from solid_principles.open_closed_principle.shape import Shape
from solid_principles.open_closed_principle.circle import Circle
from solid_principles.open_closed_principle.rectangle import Rectangle

def print_area(shape: Shape):
    print(f"The area is: {shape.area()}")

# Create shapes
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Print their areas
print_area(rectangle)  # Output: The area is: 50
print_area(circle)     # Output: The area is: 153.86