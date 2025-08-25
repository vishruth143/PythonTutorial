# From the list of numbers move all the zeros to the end of the list.

def move_all_zeroes_to_end(l):
    for num in l:
        if num == 0:
            l.remove(num)
            l.append(num)
    return l

l = [1, 0, 2, 0, 4, 6]
print(move_all_zeroes_to_end(l))
