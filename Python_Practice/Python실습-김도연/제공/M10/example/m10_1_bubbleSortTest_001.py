def bubble_sort(L):    
    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                temp = L[j+1]
                L[j+1] = L[j]
                L[j] = temp

mylist = [6,55,8,13,4,9,11,3,1,2]
print("정렬 전 : ", end='')
print(mylist)

bubble_sort(mylist)

print("정렬 후 : ", end='')
print(mylist)
