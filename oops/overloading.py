# Note: Python does not support method overloading in the traditional sense.
# The last defined method with the same name will override the previous ones.
# However, we can achieve similar functionality using default arguments or *args.

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