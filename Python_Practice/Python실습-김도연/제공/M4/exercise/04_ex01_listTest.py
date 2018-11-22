"""
리스트 사용 및 반복문

[실습]

10 미만의 자연수 두 개를 입력받아서 첫 번째 항과
두 번째 항을 입력받은 수로 초기화 시킨 후 세 번째 항부터는
전전항(첫번째 항)과 전항(두번째 항)의 합을 구하여 그 합의 1의 자리로
채워서 차례로 10개를 출력하는 프로그램을 작성하시오.
리스트와 반복문을 사용하여 작성하시오.

<입력 예>
첫번째 자리 수 입력 : 5
두번째 자리 수 입력 : 8

5 8 3 1 4 5 9 4 3 7 

<입력 예>
첫번째 자리 수 입력 : 9
두번째 자리 수 입력 : 9

9 9 8 7 5 2 7 9 6 5 
"""

num = []

tmp = int(input("첫번째 자리 수 입력 : "))
num.append(tmp)
tmp = int(input("두번째 자리 수 입력 : "))
num.append(tmp)

#------------------------------------------------
# 이 부분에 코딩하시오.

for i in range(2,10) :
    num.append((num[i-2]+num[i-1]) % 10)

#---------여기까지--------------------------------------

print()
for i in range(0, 10):
    print("{} ".format(num[i]),end="")





