# Method Overloading in Python
# Method overloading is the ability to define multiple methods with the same name but
# different parameters. Unlike languages such as Java or C++, Python does NOT support
# traditional method overloading — if you define the same method name twice, the second
# definition simply replaces the first.
# However, similar behavior can be achieved in Python using:
#   - Default arguments: def method(self, a, b=None)
#   - Variable-length arguments: def method(self, *args)
# Note: The last defined method with the same name will override the previous ones.

class A:
    def sum(self, *args):
        s = 0
        for item in args:
            s += item
        return s

obj = A()
print(obj.sum(2, 3))        # 5
print(obj.sum(2, 3, 4))     # 9
print(obj.sum(2, 3, 4, 5))  # 14