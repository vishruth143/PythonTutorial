"""
Examples to show how strings work in python

Sequence of characters
Contains a-z, A-Z, 0-9, `~!@#$%^&*()-_=+;:'",<.>/?[{]}\|
In double or single quotes
"""

a = "This is a simple string"
b = 'Using single quotes'
print(a)
print(b)

c = 'Need to use "quotes" inside a string'
print(c)
c = "Need to use 'quotes' inside a string"
print(c)

d = "Another way to handle \"quotes\""
print(d)

a = "This is a single \
string"
print(a)

print("*"*20)

print('Hello, {}'.format('Vishva'))
print("Sammy has {} balloons.".format(5))

str = 'Docupace_Reference_Value'
print(str.find('Docupace_Reference_Value'))