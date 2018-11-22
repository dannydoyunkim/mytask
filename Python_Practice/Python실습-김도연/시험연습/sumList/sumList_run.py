from sumList import *

input1 = [ 7, 1, 6 ]
input2 = [ 5, 9, 2 ]
result = [ 0, 0, 0 ]

printList(input1)
printList(input2)

# 두개의 배열에 저장된 숫자를 역순으로 꺼내 합한다.
addList(result, input1, input2)

printList(result)
