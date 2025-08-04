def my_func(e):
    return len(e)

l= ['Ford', 'Mitsubishi', 'BMW', 'VW']
l.sort(key=my_func)
print(l)