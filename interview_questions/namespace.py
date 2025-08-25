# Built-in Namespace

print(len("hello"))   # 'len' is a built-in function

# Global Namespace
x = 10  # Global variable

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        z = 30  # Local variable
        print("Local z:", z)       # 30
        print("Enclosing y:", y)   # 20
        print("Global x:", x)      # 10
        print("Built-in len:", len("Python"))  # 6

    inner_function()

outer_function()

