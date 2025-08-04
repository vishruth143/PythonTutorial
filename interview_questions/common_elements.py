# Write python program to find the common elements between two lists.
def common_elements(l1, l2):
    common = []
    for num in l1:
        if num in l2:
            common.append(num)
    return common

l1 = [2, 3, 4, 5, 6]
l2 = [6, 5, 4, 3, 0]
print(common_elements(l1, l2))