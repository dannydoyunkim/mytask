myList = [7,4,9,1,33,11,2,6,10,12,16,5]
print("원본자료 : ", myList)
val = int(input("검색 값 : "))

print("index() 함수로 유무 확인 결과")
try:
    res = myList.index(val)
    print("{}값이 인덱스{}에포함되어 있습니다.".format(val, res))
except ValueError:    
    print("{}값이 포함되어 있지 않습니다. ".format(val))






   

