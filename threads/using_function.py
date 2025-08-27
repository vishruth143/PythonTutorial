from threading import *

def display_numbers():
    i = 0
    print(current_thread().name)
    while i < 10:
        print(i)
        i += 1

print(current_thread().name)
t = Thread(target=display_numbers)
t.start()
