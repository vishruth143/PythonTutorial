def decorate_fun(func):                     # ① A decorator function that takes another function as input
    def inner_fun():                        # ② Inner function that wraps the original function
        print("I got decorated")            # ③ Extra behavior before the original function runs
        func()                              # ④ Call the original function
    return inner_fun                        # ⑤ Return the new wrapped function

@decorate_fun
def original_fun():
    print("Original function")

original_fun()