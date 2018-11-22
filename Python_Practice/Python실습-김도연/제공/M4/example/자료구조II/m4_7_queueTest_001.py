queue = []            
queue.append('A')
print("PUT 'A' 후 큐 : ", queue)
queue.append('B')
print("PUT 'B' 후 큐 : ", queue)
queue.append('C')
print("PUT 'C' 후 큐 : ", queue)
queue.append('D')
print("PUT 'D' 후 큐 : ", queue)

print()
while queue:
    print("{}가 GET된 후 큐 : {} ".format(queue.pop(0), queue))
