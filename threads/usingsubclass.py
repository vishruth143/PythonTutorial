from threading import Thread, current_thread


class MyThread(Thread):
    def run(self):
        i = 0
        print(current_thread().name)
        while i < 10:
            print(i)
            i += 1

print(current_thread().name)
t = MyThread()
t.start()