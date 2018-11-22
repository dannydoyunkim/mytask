import threading
import time

class Account:
    balance = 1000

    def getBalance(self):
        return self.balance

    def withdraw(self, money):
        if self.balance >= money:
            time.sleep(0.1)
            print("\n{} balance : {}".format(threading.currentThread().getName(),self.balance), end='')
            self.balance -= money
            print("\n{} balance : {}".format(threading.currentThread().getName(),self.balance), end='')

            
account = Account()

class ThreadAccount(threading.Thread) :     
    def run(self) :        
        while account.getBalance() > 0 : 
            account.withdraw(100)
            

myAcc1 = ThreadAccount(name="Mom")
myAcc2 = ThreadAccount(name="Daughter")

myAcc1.start()
myAcc2.start()
