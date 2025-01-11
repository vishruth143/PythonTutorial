if __name__ == '__main__':
    print("Enter x: ")
    x = int(input())

    print("Enter y: ")
    y = int(input())

    print("Enter z: ")
    z = int(input())

    print("Enter n: ")
    n = int(input())

    # List comprehension to generate coordinates
    result = [[i, j, k] for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]

    print(result)