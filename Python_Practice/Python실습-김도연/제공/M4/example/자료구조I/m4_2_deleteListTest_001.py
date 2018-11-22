myList = [1,2,3,4,5,6,7,8,9,10]

myList[2:4] = []
print("1 :", myList)


del(myList[2]) ;print("2 :", myList)
del(myList[-2]);print("3 :",myList)
del(myList[1:3]);print("4 :",myList)
del(myList[:]);print("5 :",myList)
del myList ; print("6 :",myList)
