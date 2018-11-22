# 리스트 출력 확인하기
#
# list1 = [2,4,6]
# list2 = ['2','4','6']
#
# print(list1) # 숫자리스트
# print(list2) # 문자리스트

## 다시 만들기

list1 = [1,2,3,4,5,6,7,8,9,10]

print(list1) # 프린트 함수로 출력하면 모양데로 나옴

for i in list1 : # list1의 데이터에서 하나씩 맵핑해줌
    print(i)

print("list의 길이 :",len(list1))

for i in range(0,len(list1)) : # len을 사용하면 list나 string의 개수를 알 수 있다.
    print(list1[i])             # 이와 같이 index를 통해서 값을 가져올 수 있다.

# list내의 값들의 합 구하기
# 방식 1
total = 0

for i in list1 :
    total = total + i
print(total)

# 방식 2
total = 0

for i in range(len(list1)) :
    total = total + list1[i]
print(total)

# list 다루기
# list.append(something) : list의 마지막 위치에 something을 추가함.

# designated 정의
list1 = []

list1.append(10)
list1.append(20)
list1.append(30)

# nestedloop 정의
list2 = []

#---------------------하기 코드는 에러가 난다. input 값은 String이기 때문이다. ------------------------
# for i in range(10) :
#     list2.append(input("값 입력 :"))
#
# print(list1)
# for i in list2 :
#     total += i
#     print(i)
#
#---------------------------------------------

# ---------------------하기 코드는 에러가 난다. input 값은 String이기 때문이다. ------------------------
for i in range(10):
    list2.append(int(input("{} 째값 입력 :".format(i+1))))

print(list2)

for i in list2:
    total += i
    print(i)

# ---------------------------------------------