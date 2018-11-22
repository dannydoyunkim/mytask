def quickSort(arr):
    if len(arr) <= 1:
        return arr      
    i = len(arr) // 2
    pivot = arr[i]
    left = []; mid = []; right = []
    
    for x in arr:
        if x < pivot:     left.append(x)     
        elif x == pivot:  mid.append(x)    
        elif x > pivot:   right.append(x)    
    
    return quickSort(left) + mid + quickSort(right)
       

mylist = [20,30,7,55,6,3,41,15,4,1]
print("정렬 전 : ", end='')
print(mylist)

res = quickSort(mylist)

print("정렬 후 : ", end='')
print(res)
