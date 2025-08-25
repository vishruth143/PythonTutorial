# Example of Inheritance in Python

class Parent:
    def __init__(self):
        self.parent_attribute = "I am a parent attribute"

    def parent_method(self):
        return "This is a method from the Parent class"

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of the Parent class
        self.child_attribute = "I am a child attribute"

    def child_method(self):
        return "This is a method from the Child class"

    def parent_method(self):
        return super().parent_method()

    def overridden_parent_method(self):
        # Overriding the parent method
        return "This is an overridden method from the Child class"

# Example usage
if __name__ == "__main__":
    child_instance = Child()
    print(child_instance.parent_attribute)  # Accessing parent attribute
    print(child_instance.child_attribute)   # Accessing child attribute
    print(child_instance.child_method())    # Calling child method
    print(child_instance.parent_method())   # Calling overridden parent method
    print(child_instance.overridden_parent_method())  # Calling overridden parent method
