# Sort a list using inbuilt function
l = [ 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]

l.sort(reverse=True)
print(l)

l.sort(reverse=False)
print(l)

print(sorted(l, reverse=True))
print(sorted(l, reverse=False))