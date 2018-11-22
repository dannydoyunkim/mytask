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




