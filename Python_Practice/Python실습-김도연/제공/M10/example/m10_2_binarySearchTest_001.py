def binarySearch(array, value, low=0, high=0):
	if low > high:
		return False
	mid = (low+high) // 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid

        
    
mylist = [6,55,8,13,4,9,11,3,1,2]
mylist.sort()
print(mylist)
print("검색값 : ", end='')
search = int(input())
res = binarySearch(mylist, search)
if res != False:
    print("{}는 인덱스{}에 위치함".format(search, res))
else:
    print("{}는 포함되지 않았습니다.".format(search))
