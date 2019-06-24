"""
Built-in methods to help manipulating a list
"""

cars = ['bmw', 'honda', 'audi']
length = len(cars)
print(length)

cars.append('benz')
print(cars)

cars.insert(1, 'jeep')
print(cars)

x = cars.index('honda')
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove('jeep')
print(cars)

slicing = cars[0:2]
a = cars[1:len(cars)]
print(slicing)
print(a)
print('*'*20)
print(cars)
cars.sort()
print(cars)
