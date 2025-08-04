# Given string S, reverse the string without reversing its individual words. Words separated by dots
def reverse_individual_words(data_string):
    return '.'.join(data_string.split(".")[::-1])

s = 'i.like.this.program.very.much'
print(reverse_individual_words(s))