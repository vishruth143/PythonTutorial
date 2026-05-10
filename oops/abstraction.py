# Abstraction in Python
# Abstraction is the concept of hiding the internal implementation details and showing only
# the essential features of an object. It helps reduce complexity by allowing the programmer
# to focus on what an object does rather than how it does it.
# In Python, abstraction is achieved using Abstract Base Classes (ABC) from the `abc` module.
# A class that contains one or more abstract methods is called an abstract class.
# Abstract methods are declared but contain no implementation — subclasses MUST override them.

from abc import ABC, abstractmethod

class Shape(ABC):   # Abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
c = Circle(5)
print("Area:", c.area())          # 78.5
print("Perimeter:", c.perimeter())# 31.4
