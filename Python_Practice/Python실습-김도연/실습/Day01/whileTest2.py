# value = 1
#
# while value <= 100 :
#     value = int(input('값 입력 : '))
#     print("입력한 값 :", value)
#
#
value = 1

while True : # 무한 루프이므로 break를 써서 종료해야함
    value = int(input('숫자 입력 : '))
    if value < 0 :
        break
    print("입력한 값 :", value)