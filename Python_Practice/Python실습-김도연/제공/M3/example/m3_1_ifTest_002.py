#m3_1_ifTest_002.py

result = 0
print("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈")
op = int(input("선택 :"))
num1 = int(input("값1 :"))
num2 = int(input("값2 :"))

if(op == 1):
    result = num1 + num2

if(op == 2):
    result = num1 - num2

if(op == 3):
    result = num1 * num2

if(op == 4):
    result = num1 / num2

print("결과 {}".format(result))    


