"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""


def sum_nums(n1=2, n2=4):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(2,8)
print(sum1)
sum1 = sum_nums()
print(sum1)
sum1 = sum_nums(n2=12, n1=8)
print(sum1)
sum1 = sum_nums(1)
print(sum1)

def sum_nums(n1, n2=4):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, n2=8)
print(sum1)
sum1 = sum_nums(1)
print(sum1)