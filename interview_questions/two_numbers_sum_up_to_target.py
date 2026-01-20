# Find the pair of numbers in a given list which sum up to the target
l = [2, 7, 11, 15]

target = 9
num_pair = (None, None)
for i in range(len(l)-1):
    sum_res = l[i] + l[i+1]
    if sum_res == target:
        num_pair = (l[i], l[i+1])

print(num_pair)