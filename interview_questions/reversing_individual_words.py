# Given string S, reverse the string without reversing its individual words. Words separated by dots

def reverse_individual_words(data_string):
    return '.'.join(data_string.split(".")[::-1])

s = 'i.like.this.program.very.much'
print(reverse_individual_words(s))

# Step 1: Split the string based in the separator .
# s = 'i.like.this.program.very.much'
# l = s.split('.')
# print(l)

# Step 2: Get the length of the list.
# l_len = len(l)
# print(l_len)

# Step 3: Loop through the list and reverse the list
# result = []
# for i in range(l_len):
#     result.append(l[l_len - 1])
#     l_len -= 1

# Step 4: Join the list
# print(" ".join(result))
