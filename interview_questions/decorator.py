# def decorate_fun(func):                     # ① A decorator function that takes another function as input
#     def inner_fun():                        # ② Inner function that wraps the original function
#         print("I got decorated")            # ③ Extra behavior before the original function runs
#         func()                              # ④ Call the original function
#     return inner_fun                        # ⑤ Return the new wrapped function
#
# @decorate_fun
# def original_fun():
#     print("Original function")
#
# original_fun()

import time

def time_logger(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
    return wrapper

@time_logger
def process_data():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

process_data()