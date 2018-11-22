my_list = [1, 2, 3, 4, 5]

print("첨자를 입력하세요:")

try:    
    index = int(input("인덱스 입력 :" ))
    value = int(input("정수 입력 :" ))
    result = my_list[index]/value
    print("result = {}".format(result))
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("정수값으로 입력해야합니다.")
except IndexError:
    print("잘못된 첨자입니다.")
else:
    print("리스트의 요소 출력에 성공했습니다.")
finally:
    print("무조건 처리되는 코드입니다.")
