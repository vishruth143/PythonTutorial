class Fruit(object):

    def __init__(self):
        print("I'm a fruit")

    def nutrition(self):
        print("I'm full of vitamins")

    def fruit_shape(self):
        print("Every fruit can have different shape")

class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("I'm an Orange")

    def nutrition(self):
        print("I'm full of vitamin C")

    def color(self):
        print("I keep it simple, the color is also orange")

f = Fruit()
f.nutrition()
f.fruit_shape()

o = Orange()
o.nutrition()
o.fruit_shape()
o.color()


