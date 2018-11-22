class MyStack():
   def __init__(self, max_length=50):
     self.items = []
     self.top = 0  # top에는 데이터를 저장할 최신 위치를 가르킨다.
     self.max_length = max_length

   def push(self, data):
     if self.is_full():  # push할 수 있는지 확인
       raise Exception('스택이 꽉 찼습니다!')

     self.items.append(data)
     self.top += 1

   def pop(self):
     if self.is_empty(): # pop할 수 있는지 확인
       raise Exception('스택이 비었습니다!')

     self.top -= 1
     data = self.items[self.top]
     del self.items[self.top + 1]

     return data

   def peek(self):
     if self.is_empty():
       raise Exception('스택이 비었습니다!')

     return self.items[self.top - 1] # pop예정인 데이터를 참조한다.

   def is_empty(self):
     return self.top == 0  # top이 0이면, 저장된 데이터가 하나도 없는 것임

   def is_full(self):
     # top이 max_length와 동일하다는 것은 꽉 찬것임.
     return self.top == self.max_length

   def display(self):
     for index in range(self.top):
       print(self.items[index])



myStack = MyStack()
myStack.push(10)
myStack.push(20)
myStack.display()
