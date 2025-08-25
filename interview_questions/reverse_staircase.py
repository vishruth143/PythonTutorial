# Print the reverse staircase to the given number

def staircase(num):
    for i in range(1, num+1):
        print(' '*(num-i)+'*'*i)

staircase(10)
