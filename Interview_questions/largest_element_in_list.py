# Write design_pattern Python program to find the largest element in design_pattern list.
def largest(data_list):
    largest_num = data_list[0]
    for num in l:
        if num > largest_num:
            largest_num = num
    return largest_num

l = [5, 6, 3, 2, 1, 34]
print(largest(l))