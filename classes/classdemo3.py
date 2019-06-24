"""
Object Oriented Programming
"""

class Car(object):

    # Memeber varibles which are available to all the members of the class
    wheels = 4

    def __init__(self, make, model):
        # Instance variables change with each instance of the class
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)

c1 = Car('bmw', '550i')
print(c1.make)
c1.wheels = 3
print(c1.wheels)
# c1.info()

# print()
# print('#'*30)
# print()

c2 = Car('benz', 'E350')
print(c2.make)
print(c2.wheels)
# c2.info()

print(Car.wheels)
