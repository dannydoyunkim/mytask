val1 = int(input("정수1 : "))
val2 = int(input("정수2 : "))

try:
    result = val1 / val2
    print("{} / {} = {}".format(val1, val2, result))
except:
    print("0으로 나눌 수 없습니다")


