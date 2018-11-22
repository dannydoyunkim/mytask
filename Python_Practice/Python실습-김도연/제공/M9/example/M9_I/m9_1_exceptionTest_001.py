# 원본
# val1 = int(input("정수1 : "))
# val2 = int(input("정수1 : "))
# 
# 
# result = val1 / val2
# 
# print("{} / {} = {}".format(val1, val2, result))



val1 = int(input("정수1 : "))
val2 = int(input("정수1 : "))

try :
    result = val1 / val2

    print("{} / {} = {}".format(val1, val2, result))

except :
    print("0으로 나누면 안됨")

val1 = int(input("정수1 : "))
val2 = int(input("정수1 : "))

try :
    result = val1 / val2

    print("{} / {} = {}".format(val1, val2, result))

except ZeroDivisionError as err :
    print("0으로 나누면 안됨")