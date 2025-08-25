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