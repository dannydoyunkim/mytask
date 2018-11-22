val1, val2 = 0,0

try :
    val1 = int(input("정수1 : "))
    val2 = int(input("정수1 : "))
except ValueError as err :
    print("예외 이유는? {}".format(err))

try :
    result = val1 / val2

    print("{} / {} = {}".format(val1, val2, result))

except BaseException as err :
    print("예외 이유는? {}".format(err))