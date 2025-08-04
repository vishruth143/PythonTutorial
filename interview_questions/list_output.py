# Guess the output of the following code snippet
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element
    return v

print(fun(data[0]))