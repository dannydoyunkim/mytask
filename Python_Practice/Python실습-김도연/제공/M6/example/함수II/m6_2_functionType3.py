def functionType3():
    sum = 0
    for i in range(11):
        sum += i
    return sum    
        


result = functionType3()
print("함수 호출 결과(변수이용) : ", result)
    
print("함수 호출 결과(변수없음) : ", functionType3())
