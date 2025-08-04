# Write python program to count the frequency of each element in list.
def frequency_of_each_element(data_list):
    frequency = {}
    for num in data_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

l = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print(frequency_of_each_element(l))