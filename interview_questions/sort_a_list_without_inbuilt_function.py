# Sort in descending order
data_list = [ 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]
sorted = []

while data_list:
    maximum = data_list[0]
    for num in data_list:
        if num > maximum:
            maximum = num
    sorted.append(maximum)
    data_list.remove(maximum)

print(sorted)

# Sort in ascending order
data_list = [ 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]
sorted = []
while data_list:
    minimum = data_list[0]
    for num in data_list:
        if num < minimum:
            minimum = num
    sorted.append(minimum)
    data_list.remove(minimum)

print(sorted)
