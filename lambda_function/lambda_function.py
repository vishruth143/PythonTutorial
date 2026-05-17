# Lambda Function Tutorial in Python
# A lambda is a small anonymous (nameless) function.
# Syntax:
#   lambda arguments: expression
# It is useful for short, one-line operations.

# 1) Add two numbers
# This lambda takes two inputs (a, b) and returns their sum.
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# 2) Multiply two numbers
# This lambda returns the product of two numbers.
mul = lambda a, b: a * b
print(mul(2, 3))  # Output: 6

# 3) Convert text to uppercase
# This lambda takes a string and converts it to uppercase using .upper().
upper = lambda s: s.upper()
print(upper("python"))  # Output: PYTHON

# 4) Find the bigger number
# This lambda uses a conditional expression:
# return a if a is greater than b, otherwise return b.
bigger = lambda a, b: a if a > b else b
print(bigger(2, 3))  # Output: 3
