stack = []            
stack.append('A')
print("PUSH 'A' 후 스택 : ", stack)
stack.append('B')
print("PUSH 'B' 후 스택 : ", stack)
stack.append('C')
print("PUSH 'C' 후 스택 : ", stack)
stack.append('D')
print("PUSH 'D' 후 스택 : ", stack)

print()
while stack:
    print("{}가 POP된 후 스택 : {} ".format(stack.pop(), stack))
