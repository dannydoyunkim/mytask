mySet1 = set([100,300,"python",3.14])
mylist1 = list(mySet1)

print("Set : ", mySet1)
print("List : ", mylist1)  

print("첫번째 인덱스의 값 : ", mylist1[0])  

mySet1.add(1)
mySet1.add(20)

mylist2 = list(mySet1)

print("\n 데이터 추가 후")
print("Set : ", mySet1)
print("List : ", mylist2)  

print("첫번째 인덱스의 값 : ", mylist2[0])



