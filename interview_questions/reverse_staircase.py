# Print the reverse staircase to the given number

def reversed_staircase(num):
    for i in range(1, num+1):
        print((' '*(num-i)) + ('*'*i))

reversed_staircase(10)
