"""
Examples to show available string methods in python
"""
# Strings are immutable
# Accessing characters in string
#index starts from 0
first = "nyc"[0]
print(first)
first = "nyc"[1]
print(first)
first = "nyc"[2]
print(first)

city = "sfo"
ft = city[0]
print(ft)

"""
len()
lower()
upper()
str()
"""

stri = "This is a Mixed case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + " " + str(2))

"""
Concatenation
"""
print("Hello "+" "+" World!!!")
print(first+" "+city)

# Replace Method
a = "1abc2abc3abc4abc"
print("*****************")
print(a)
print(a[1:])
print(a[:6])
print(a[:])
print(a[-1])
print(a[-2])
print(a[:-1])
print(a[:len(a)])
print(a[:len(a)-1])
print(a[:len(a)-2])
print(a[::])
print(a[::1])
print(a[::2])
print(a[::-1])
print(a)
print("*****************")

print(a.replace('abc', 'ABC'))
print(a.replace('abc', 'ABC', 1))

# Sub-string
# Starting index is inclusive
# Ending index is exclusive
sub = a[1]
print("*****************")
print(sub)
sub = a[1:6]
print(sub)
step = a[1:6:1]
print(step)
step = a[1:6:2]
print(step)
step = a[1:6:3]
print(step)