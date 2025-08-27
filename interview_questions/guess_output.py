# What is the output of the code below?

# Problem 1 – Dictionary comprehension with multiple if conditions
print('*'*10+'Problem 1'+'*'*10)
dict1 = {i: i + 1 for i in range(10) if i % 2 == 0 if i % 3 == 0}
print(dict1)

# Problem 2 - Looping with range
print('*'*10+'Problem 2'+'*'*10)
print('*'*20)
for i in range(10):
    print(i)

# Problem 3 – String interning
print('*'*10+'Problem 3'+'*'*10)
a = "python"
b = "python"
c = "".join(["py", "thon"])
print(a == b, a is b)
print(a == c, a is c)

# Problem 4 – Nested indexing
print('*'*10+'Problem 4'+'*'*10)
names = ['Bangalore', 'Jhon', 'India']
print(names[-1][-2])

# Problem 5 – List, generator, and dictionary comprehensions
print('*'*10+'Problem 5'+'*'*10)
mylist1 = [x*x for x in range(3)]
mylist2 = (x**x for x in range(3))
mylist3 = {x: x+x for x in range(1, 3)}
print(mylist1)
print(list(mylist2))
print(mylist3)

# Problem 6 – Tuple immutability vs mutability inside
print('*'*10+'Problem 6'+'*'*10)
t = (1, 2, [3, 4])
t[2].append(5)
print(t)

# Problem 7 – Scope & LEGB
print('*'*10+'Problem 7'+'*'*10)
x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)

# Problem 8 – List aliasing vs copying
# aliasing, both variables point to the same list.
# copying, creates a new list.
print('*'*10+'Problem 8'+'*'*10)
a = [1, 2, 3]
b = a
c = a[:]
a[0] = 99
print("a:", a)
print("b:", b)
print("c:", c)

# Problem 9 – Mutable default argument trap
print('*'*10+'Problem 9'+'*'*10)
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

# If you want a new list every time:
# Rule of Thumb:
# Never use mutable objects (like list, dict, set) as default arguments.
# Use None as a default, and create the object inside the function.
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []   # create a fresh list
    my_list.append(value)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2]
print(append_to_list(3))  # [3]

# Problem 10 – Operator precedence
# 2 < 3 == 3 uses chained comparison (mathematical style).
# (2 < 3) == 3 uses boolean-to-int comparison because the parentheses break the chain.
print('*'*10+'Problem 10'+'*'*10)
print(2 < 3 == 3)
print((2 < 3) == 3)  # In Python, True is actually the integer 1 under the hood.

# Problem 11 – Dictionary key mutability
# Rule of thumb:
# Immutable types (int, float, string, tuple (with immutable elements), frozenset) → Can be keys.
# Mutable types (list, dict, set) → Cannot be keys.
print('*'*10+'Problem 11'+'*'*10)
my_dict = {}
my_dict[1] = "int key"
my_dict[(1, 2)] = "tuple key"
# my_dict[[1, 2]] = "list key"  # Uncomment this line
print(my_dict)

# Problem 12 – Generator exhaustion
print('*'*10+'Problem 12'+'*'*10)
gen = (x*x for x in range(3)) # This creates a generator object, not a list. It will yield values lazily (one at a time) when iterated. Values are: 0*0 = 0, 1*1 = 1, 2*2 = 4.
print(list(gen)) # Consumes the generator, output: [0, 1, 4]
print(list(gen)) # Generator is exhausted, output: []

# Problem 13 – String immutability
print('*'*10+'Problem 13'+'*'*10)
str1 = "python"
str2 = "python1"
str1[3] = "r" # This will raise an error because strings are immutable in Python. TypeError: 'str' object does not support item assignment

