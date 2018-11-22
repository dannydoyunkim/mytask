myTuple = (1,2,3,4,1,6,1,8,9,0)
myTuple2 = 'a','b','c','d'

print("myTuple = " , myTuple)
print("myTuple2 = " , myTuple2)
print("슬라이싱 결과")
print("myTuple[0:3] :",myTuple[0:3])
print("myTuple[ :3] :",myTuple[:3])
print("myTuple[3: ] :",myTuple[3:])

print("\n+, * 연산 결과")
print(myTuple + myTuple2)
print(myTuple*2)

print("\n함수 활용 결과")
print(myTuple.count(1))

val = myTuple.index(4)
print(val)

print("\n오류가 나는 이유는?")
del(myTuple[4])  
del(myTuple)     
print(myTuple)

