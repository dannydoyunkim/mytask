result = 0
print("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈")

op = int(input("선택 :"))
num1 =int(input("값 1 :"))
num2 = int(input("값 2:"))

if(op == 1) :
    result = num1 + num2
elif(op == 2 ) :
    result = num1 - num2
elif( op == 3 ) :
    result = num1 * num2
else :
    result = num1 / num2

print("결과 : {}".format(result))