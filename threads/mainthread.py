from threading import *

print("Current Thread that is running:", current_thread().name)

if current_thread() == main_thread():
    print("Main thread.")
else:
    print("Some other thread.")