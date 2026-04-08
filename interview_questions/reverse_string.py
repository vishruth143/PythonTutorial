# Write python program to reverse string

def reverse(str):
    return str[::-1]

s = "Python"
print(reverse(s))

# # Step 1: Convert the string to list
# l, rev_l = [], []
# for ch in s:
#     l.append(ch)
# print(l)
#
# # Step 2: Reverse the list
# l_len = len(l)
# for i in range(len(l)):
#     rev_l.append(l[l_len-1])
#     l_len -= 1
# print(rev_l)
#
# # Write the list as string
# print(''.join(rev_l))