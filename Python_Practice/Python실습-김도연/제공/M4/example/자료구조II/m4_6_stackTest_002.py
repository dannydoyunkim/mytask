from collections import deque

class Stack(deque):
   def push(self, x):  # push를 override 한다.
       super().appendleft(x)

   def pop(self):    # pop을 override 한다.
       super().popleft()

   def display(self):
     for node in self.__iter__():
         print(node,end='')
     print()    


st = Stack()
st.push('A')
st.push('B')
st.push('C')
st.push('D')

st.display()

print()
print("pop한 이후 ".format(st.pop()))
st.display()

print()
print("pop한 이후 ".format(st.pop()))
st.display()

print()
print("pop한 이후 ".format(st.pop()))
st.display()

print()
print("pop한 이후 ".format(st.pop()))
st.display()
