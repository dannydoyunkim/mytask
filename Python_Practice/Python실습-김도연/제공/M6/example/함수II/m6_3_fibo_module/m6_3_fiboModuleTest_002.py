from m6_3_fiboModule import fibo            #fibo 모듈 import
 
num = int(input("몇 번째 값을 계산 할까요? "))
 
fibResult = fibo(num)  #fibo 모듈의 fib2함수를 사용하여 결과를 fibResult(리스트)에 저장
for i in fibResult:
    print(i, end= ' ')
