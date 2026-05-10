def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(gen)

# 1. next() — manual, one value at a time
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# 2. for loop — most common
for num in numbers():
    print(num)  # 1, 2, 3

# 3. list() — consume all at once
print(list(numbers()))  # [1, 2, 3]
