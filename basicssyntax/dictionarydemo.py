"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1': 'v1', 'k2': 'v2'}
Not sequenced, no indexing -> mapping
Mutable
"""

car = {'make': 'bmw', 'model': '550i', 'year': '2016'}
d = {}
print(d)
print(car['make'])
model = car['model']
print(model)
print(car['year'])

d['one'] = 1
d['two'] = 2
print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)

