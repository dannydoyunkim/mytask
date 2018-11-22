def selectNumber(phoneBook, sample) :

    for read_data in sample:
        if read_data.startswith("010"):
            loc_key = "핸드폰"
        elif read_data.startswith("02"):
            loc_key = "서울"
        else:
            loc_key = "기타"

        if loc_key not in phoneBook:
            phoneBook[loc_key] = []  ## Dictionary의 value를 List로 정의해야함 phoneBook[splited_data[0]] = []
            phoneBook[loc_key].append(read_data)
        else:
            phoneBook[loc_key].append(read_data)

def printNumber(phoneBook) :

    for keys in phoneBook.keys():
        print("<{}> 지역 목록".format(keys))

        for list in phoneBook.get(keys):
            print('"{}"'.format(list))


if __name__ == "__main__" :

    sample = ["010-5464-5688",
              "02-1029-1234",
              "042-3456-1290",
              "010-1199-5678",
              "02-1029-1234",
              "032-3456-1290",
              "010-2388-1238",
              "02-1029-1234",
              "062-3456-1290",
              "062-5555-3490",
              "010-5678-6666",
              "02-1029-1234",
              "032-8796-1330",
              "010-5678-6666",
              "02-1029-1234",
              "032-8796-1330"]

    phoneBook = {}

    selectNumber(phoneBook, sample)
    printNumber(phoneBook)

# 핸드폰, 서울, 기타를 키 값으로 관리될 수 있도록 한다.

# 핸드폰 번호만 따로 저장
# 서울 전화번호만 따로 저장
# 기타 다른 지역 번호만 따로 저장
# 각각의 전화번호를 구분하여 저장하고 출력하는 프로그램을 작성하세요.

# 출력 형식
# <핸드폰> 목록
# "010-5464-5688"
# "010-1199-5678"
# "010-2388-1238"
# "010-5678-6666"
# "010-5678-6666"

# <서울> 지역 목록
# "02-1029-1234"
# "02-1029-1234"
# "02-1029-1234"
# "02-1029-1234"
# "02-1029-1234"

# <기타> 지역 목록
# "042-3456-1290"
# "032-3456-1290"
# "062-3456-1290"
# "062-5555-3490"
# "032-8796-1330"



