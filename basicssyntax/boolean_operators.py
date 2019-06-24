"""
and
***************************
True and True --> True
True and False --> False
False and False --> False

or
***************************
True or True --> True
True or False --> True
False or False --> False

not
***************************
Not True --> False
Not False --> True
"""

and_output1 = (10 == 10) and (10 > 9)
and_output2 = (10 == 10) and (10 < 9)
and_output3 = (10 != 10) and (10 < 9)
print(and_output1)
print(and_output2)
print(and_output3)

or_output1 = (10 == 10) or (10 > 9)
or_output2 = (10 == 10) or (10 < 9)
or_output3 = (10 != 10) or (10 < 9)
print(or_output1)
print(or_output2)
print(or_output3)

not_true = not(10 == 10)
print(not_true)

not_false = not(10 < 9)
print(not_false)

