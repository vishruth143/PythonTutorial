"""
Write a Python program to generate a list of all possible coordinates [i, j, k] such that:
0 ≤ i ≤ x
0 ≤ j ≤ y
0 ≤ k ≤ z
The sum i + j + k is not equal to n
Return this list as output.
"""

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
