def linearSearch2(s, key):
    i = 0
    while i < len(s):
        if s[i] == key:
            return i
        elif s[i] > key:
            return -1
        i += 1
    return -1


mylist = [1, 2, 8, 9, 11, 19, 29]
print("검색값 : ", end='')
search = int(input())
res = linearSearch2(mylist, search)
if res != -1:
    print("{}는 인덱스{}에 위치함".format(search, res))
else:
    print("{}는 포함되지 않았습니다.".format(search))
