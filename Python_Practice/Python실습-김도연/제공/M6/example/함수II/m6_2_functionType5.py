def functionType5(num1, num2):
    
    res1 = num1+num2
    res2 = num1-num2
    res3 = num1*num2
    res4 = num1/num2
    
    return res1, res2, res3, res4    
        


result = functionType5(20, 5)
print("변수 하나 이용 1 : ", result)
print("변수 하나 이용 2 : ", result[0], result[1], result[2], result[3])
 
res1, res2, res3, res4 = functionType5(20,5)

print("변수 각각 이용 : ", res1, res2, res3, res4)

res1 +=10;

print("변수 각각 이용 : ", res1, res2, res3, res4)
