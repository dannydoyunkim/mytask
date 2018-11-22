from collections import deque

myQueue = deque()

myQueue.append(1)
myQueue.append(2)
myQueue.append(3)
myQueue.append(4)


print(myQueue.popleft()) # 1
print(myQueue.popleft()) # 2
print(myQueue.popleft()) # 3
print(myQueue.popleft()) # 4
