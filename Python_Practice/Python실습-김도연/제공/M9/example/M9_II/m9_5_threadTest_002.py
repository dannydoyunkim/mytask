import threading
import time

class ThreadExtends(threading.Thread) :
    def run(self) :
        for i in range(5):
            time.sleep(0.1)
            print(threading.currentThread().getName()+'\n', end='')


myThread1 = ThreadExtends(name="First Thread")
myThread1.start() # 이제부터 myThread1은 실행되는 중이다.

for i in range(5) : # Thread와는 별도로 Main이 실행된다.
    time.sleep(0.1)
    print("Hello")