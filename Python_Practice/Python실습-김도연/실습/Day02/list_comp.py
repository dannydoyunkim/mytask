#### 하기 코드는 모두 같은 코드이다.

# 코드 1
list1 = []
for i in range(10) :
    list1.append(i*i)

print(list1)

# 코드 2



# 코드 3
# 맨 앞에 넣을 값을 쓰고 뒤에 for로 해당 변수의 변화 규칙을 기재한다.
list3 = [ i*i for i in range(10) ]

print(list3)

# 코드 3형식으로 코드해보기

# 2의 배수와 3의 배수의 합의 7의 배수인 것 찾기
# 이후 각각의 값과 찾아진 두개의 값을 곱한 값을 구하라

# 정상 코드
list4 = []

for i in range(2,20,2) : # 2의 배수
    for j in range(3,20,3) : # 3의 배수
        if (i+j) % 7 == 0 : # 두개를 더한 것이 7의 배수인 것 찾기
            list4.append([i,j,i*j]) # 각각의 i, j 그리고, 두수를 곱한 값을 리스트로 넣어라

print(list4)

# 단축 코드 ---> 교재의 M4의 6 Page에 동일 패턴이 있음
list5 = [[i,j,i*j] for i in range(2,20,2) for j in range(3,20,3) if (i+j) % 7 == 0 ]

print(list5)

##### 시험가능 문제
## 상기 결과에서 i*j의 곱을 기준으로 오름차순 Sort하시요.
# [[2, 12, 24], [4, 3, 12], [6, 15, 90], [8, 6, 48], [10, 18, 180], [12, 9, 108], [16, 12, 192], [18, 3, 54]]