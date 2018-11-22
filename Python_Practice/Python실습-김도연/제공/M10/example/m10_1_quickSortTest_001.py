def partition(arr, begin, end):
    left = begin;
    right = end; 
    pivot = arr[(left + right) // 2];
 
    while (left < right):
        while ((arr[left] < pivot) and (left < right)):
            left +=1   
        while ((arr[right] > pivot) and (left < right)):
            right -=1            
 
        if (left < right):
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp  
    
    return left

def quickSort(arr, begin, end):    
    if (begin < end):
        p = partition(arr, begin, end)        
        quickSort(arr, begin, p - 1)
        quickSort(arr, p + 1, end)


mylist = [20,30,7,55,6,3,41,15,4,1]
print("정렬 전 : ", end='')
print(mylist)

quickSort(mylist,0,9)

print("정렬 후 : ", end='')
print(mylist)
