def primeNumber(data):

    priList=[]

#------------------------------------------------
# 이 부분에 코딩하시오.
    datarange = []
    priListcnt = 0

    for datarange in data.split() :
        priList.append(int(datarange))

    print(priList)

    for i in range(int(priList[0]),int(priList[1])+1) :
       primecnt = 0

       for j in range(1,i+1) :
           if ( i % j == 0 ) :
                primecnt += 1
       if(primecnt == 2) :
            priList.append(i)
            priListcnt += 1

    priList.append(priListcnt)

#---------여기까지--------------------------------------

    return priList
