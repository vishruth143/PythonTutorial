# Sort short names to long names in a list using inbuilt function

def my_func(e):
    return len(e)

l= ['Ford', 'Mitsubishi', 'BMW', 'VW']
l.sort(key=my_func)
print(l)
