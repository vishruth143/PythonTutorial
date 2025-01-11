# Swap two numbers in python
def swap(a, b):
     a, b = b, a
     return a, b

a, b = swap(2 ,3)
print(f'a: {a}, b: {b}')