def linearSearch(s, key):
    i = 0
    while i < len(s):
        if s[i] == key:
            return i
        i += 1
    return -1


mylist = [8,30,1,9,11,19,2]
print("검색값 : ", end='')
search = int(input())
res = linearSearch(mylist, search)
if res != -1:
    print("{}는 인덱스{}에 위치함".format(search, res))
else:
    print("{}는 포함되지 않았습니다.".format(search))
