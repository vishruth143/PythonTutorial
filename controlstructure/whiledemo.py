"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
x = 0
while x < 10:
    print("The value of x is:" + str(x))
    x = x + 1

a = []
num = 0
while num < 10:
    a.append(num)
    num += 1
    print("Value of num is: " + str(num))

print(a)
