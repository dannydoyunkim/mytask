my_list = [1, 2, 3, 4, 5]

print("첨자를 입력하세요:")

try:    
    index = int(input("인덱스 입력 :" ))
    result = my_list[index]/0
    print("result = {}".format(result))
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("정수값으로 입력해야합니다.")
except IndexError:
    print("잘못된 첨자입니다.")    
