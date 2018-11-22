def functionType4(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum    
        


num = int(input("더할 범위 입력 : "))
result = functionType4(num)
print("함수 호출 결과(변수이용) : ", result)
 
print("함수 호출 결과(변수없음) : ", functionType4(num))

