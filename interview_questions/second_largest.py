# Write python program to find the second largest number in list.
def second_largest(data_list):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in data_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

l = [4, 5, 6, 7, 8, 10]
print(second_largest(l))