# Using arithmetic characters
def swap(a, b):
# Using assignment operator
    a, b = b, a
    return a, b

# Using addition and subtraction
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b

# Using multiplication and division
#     a = a * b
#     b = a / b
#     a = a / b
#     return a, b

a, b = swap(2 ,3)
print(f'a: {a}, b: {b}')
