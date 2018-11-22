print("1. 리스트 sort() 함수 오름차순 정렬 결과")
myList = [7,4,9,1,33,11,2,6,10,12,16,5]
print("원본자료 : ", myList)
myList.sort()
print("오름차순 : ", myList)

print("\n2. 리스트 sort(reverse=True) 함수 내림차순 정렬 결과")
myList = [6.7, 4.1, 1.0, 2.2, 0.5, 8.1, 2.2]
print("원본자료 : ", myList)
myList.sort(reverse = True)
print("내림차순 : ",myList)

print("\n3. 리스트 사본 정렬 sorted() 함수 오름차순 결과")
myList = [7,4,9,1,33,11,2,6,10,12,16,5]
print("원본자료 : ", myList)
sortedResult3 = sorted(myList)
print("사본정렬 : ", sortedResult3)
print("원본확인 : ", myList)

print("\n4. 리스트 사본 정렬 sorted(reverse=True) 함수 내림차순 결과")
myList = ['lee','park','choi','hong','song','kim']
print("원본자료 : ", myList)
sortedResult4 = sorted(myList, reverse = True)
print("사본정렬 : ", sortedResult4)
print("원본확인 : ", myList)
