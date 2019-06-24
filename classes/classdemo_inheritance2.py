class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        super(BMW, self).drive()
        print("BMW car started")

    def headsup_display(self):
        print("This is a unique feature")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
b.headsup_display()