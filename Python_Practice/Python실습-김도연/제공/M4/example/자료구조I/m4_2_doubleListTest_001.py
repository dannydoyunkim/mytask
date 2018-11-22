doubleList = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    print("{} 번 리스트 값 입력".format(i+1))
    for j in range(4):
        doubleList[i][j] = int(input("value {}: ".format(j+1)))
    
for step in doubleList:
    for val in step:
        print(val, ' ', end='')
    print()

