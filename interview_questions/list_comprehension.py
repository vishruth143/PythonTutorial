# List Comprehension in Python
# List comprehension is a concise way to create lists using a single line of code.
# It is more readable and faster than using a traditional for loop with append().
# Syntax: [expression for item in iterable if condition]
#   - expression : the value to include in the list
#   - iterable   : the sequence to iterate over
#   - condition  : (optional) filter — only items that pass are included

print([i for i in range(10) if i%2 == 0])