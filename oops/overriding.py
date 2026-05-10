# Method Overriding in Python
# Method overriding occurs when a child class defines a method with the SAME name as one
# in its parent class. The child's version replaces (overrides) the parent's version
# when called on a child object.
# This is a key part of polymorphism — the same method name behaves differently depending
# on which class the object belongs to.
# Use `super()` if you want to call the parent's version alongside the child's logic.

class Animal:
    def speak(self):
        return "Some generic animal sound..."

class Dog(Animal):
    def speak(self):
        # Overriding the parent's speak() method with Dog-specific behavior
        return "Woof!"

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        # Overriding the parent's speak() method with Cat-specific behavior
        return "Meow!"

class Duck(Animal):
    def speak(self):
        # Calling the parent method first, then adding extra behavior
        parent_sound = super().speak()
        return f"{parent_sound} ...but also: Quack!"

# Usage
animals = [Animal(), Dog(), Cat(), Duck()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")
