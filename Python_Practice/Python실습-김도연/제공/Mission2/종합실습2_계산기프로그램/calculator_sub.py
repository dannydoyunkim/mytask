def calculator(dataList):
 #------------------------------------------------
# 이 부분에 코딩하시오.
#print(dataList)

    i = dataList.split()

    if i[1] == '*' :
        result = int(i[0]) * int(i[2])
    elif i[1] == '+':
        result = int(i[0]) + int(i[2])
    elif i[1] == '-':
        result = int(i[0]) - int(i[2])
    elif i[1] == '%':
        if( int(i[2]) <= 0 ) :
            print("{} {} {} (나누는 수가 0이면 처리 불가능)".format(i[0], i[1], i[2]))
            result = 'error1'
        else :
            result = int(i[0]) % int(i[2])
    elif i[1] == '/':
        if (int(i[2]) <= 0):
            print("{} {} {} (나누는 수가 0이면 처리 불가능)".format(i[0], i[1], i[2]))
            result = 'error1'
        else:
            result = int(i[0]) / int(i[2])
    elif i[1] == '//':
        if (int(i[2]) <= 0):
            print("{} {} {} (나누는 수가 0이면 처리 불가능)".format(i[0], i[1], i[2]))
            result = 'error1'
        else:
            result = int(i[0]) // int(i[2])
    else :
        result = 'error2'

    if(result != 'error1' and result != 'error2') :
        print("{} {} {} = {}".format(i[0], i[1], i[2], result))
    elif result == 'error2' :
        print('알 수 없는 연산자 입니다.')

#---------여기까지--------------------------------------