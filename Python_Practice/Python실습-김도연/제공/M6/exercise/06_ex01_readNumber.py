'''
[실습]
숫자를 입력받아서 한글로 출력하는 함수를 구현하고자 합니다.
즉 입력이 숫자로 6785 입력되면 이를 한글로 '육천칠백팔십오'로 변환하여 출력되도록
프로그램을 구현합니다. 이 때 숫자의 범위는 1~99999로 한다.

<요구사항>
파이썬 divmod(n, m) 함수는 n를 m으로 나눈 몫과 나머지를 한꺼번에 계산해주는 내장함수이다.
이 함수를 활용할 수 있는 방법을 생각해보시오.
(예) divmod(9, 4) => (2, 1)로 몫이 2이고 나머지가 1로 계산된다.


<입력, 출력 예>
숫자 입력 : 6785
육천칠백팔십오

숫자 입력 : 123
일백이십삼

숫자 입력 : 76834
칠만육천팔백삼십사
'''


def readNumber(n):
    result = [] 

    units = [''] + list('십백천만') 
#------------------------------------------------
# 이 부분에 코딩하시오.













#---------여기까지--------------------------------------     
    return ''.join(result[::-1])



num = int(input("숫자 입력 : "))

print(readNumber(num))
