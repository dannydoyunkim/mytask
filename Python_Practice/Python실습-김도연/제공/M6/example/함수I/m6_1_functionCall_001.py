

def calc(oper, num1, num2) :
    res = 0
    if oper == '+':
        res = num1 + num2
    elif oper == '-':
        res = num1 - num2
    elif oper == '*':
        res = num1 * num2
    elif oper == '/':
        res = num1 / num2
    else:
        print("연산자 오류입니다.")
        res = -1
    return res    


result = calc('+',10,20)
print("1 :", result)
