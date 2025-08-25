# Print the Centered staircase to the given number

def centered_staircase(num):
    for i in range(1, num+1):
        spaces = ' ' * (num-i)
        stars = '*' * (2 * i -1)
        print(spaces + stars + spaces)

centered_staircase(10)
