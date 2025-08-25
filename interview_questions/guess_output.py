# What is the output of the code below?
print('*'*10+'Problem 1'+'*'*10)
dict1 = {i: i + 1 for i in range(10) if i % 2 == 0 if i % 3 == 0}
print(dict1)

# What is the output of the code below?
print('*'*10+'Problem 2'+'*'*10)
print('*'*20)
for i in range(10):
    print(i)

# What is the output of the code below?
print('*'*10+'Problem 3'+'*'*10)
str1 = "python"
str2 = "python1"
try:
    str1[3] = "r"
except TypeError as e:
    print("Error:", e)

print(str1)

# What is the output of the code below?
print('*'*10+'Problem 4'+'*'*10)
names = ['Bangalore', 'Jhon', 'India']
print(names[-1][-2])

# What is the output of the code below?
print('*'*10+'Problem 5'+'*'*10)
mylist1 = [x*x for x in range(3)]
mylist2 = (x**x for x in range(3))
mylist3 = {x: x+x for x in range(1, 3)}
print(mylist1)
print(list(mylist2))
print(mylist3)
