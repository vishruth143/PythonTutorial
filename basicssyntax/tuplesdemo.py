"""
Tuple
like list but they are immutable
It means you can't change them
"""

my_list = [1, 2, 3]
print(my_list)

my_list[0] = 0
print(my_list)

my_tuple = (1, 2, 3, 2, 2, 3)
print(my_tuple)

print(my_tuple[0])

print(my_tuple[1:])

print(my_tuple.index(3))

print(my_tuple.count(2))

print(my_tuple.__contains__(1))
