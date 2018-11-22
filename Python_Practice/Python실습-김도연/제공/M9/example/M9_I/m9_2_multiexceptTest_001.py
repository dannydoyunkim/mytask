try:
    val1 = int(input("정수1 : "))
    val2 = int(input("정수2 : "))
    result = val1 / val2
    print("{} / {} = {}".format(val1, val2, result))
except ZeroDivisionError as err:
    print("예외 이유는? {}".format(err))
except ValueError as err:
    print("예외 이유는? {}".format(err))    


