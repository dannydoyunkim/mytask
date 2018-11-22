import threading
import time

class ThreadExtends1(threading.Thread) :
    def run(self) :
        for i in range(100):
            time.sleep(1)
            print("|",end='')

class ThreadExtends2(threading.Thread) :
    def run(self) :
        for i in range(100):
            time.sleep(1)
            print("-",end='')            


myThread1 = ThreadExtends1()
myThread2 = ThreadExtends2()

myThread1.start();
myThread2.start();


