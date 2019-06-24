"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""


def sum_nums(n1, n2):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


string_add = sum_nums('one', 'two')
print(string_add)

sum1 = sum_nums(2,8)
print(sum1)
sum2 = sum_nums(3,3)
print(sum2)
print("******************************************")

l=[1, 2, 3]
l.append(4)
print(l)
print(len(l))
print("******************************************")


def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False


x = isMetro('nyc')
print(x)
x = isMetro('boston')
print(x)
