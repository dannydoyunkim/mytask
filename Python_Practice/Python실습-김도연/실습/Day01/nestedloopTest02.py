i, j = 0, 0

# for i in range(2,10,1) :
#     for j in range(1,10,1) :
#         print("%d x %d = %2d" % (i,j,i*j))
#     print("")

# 옆으로 나열해서 구구단을 출력해보자. 아래처럼
for j in range(1,10,1) :
    for i in range(2,10,1) :
        print("%d x %d = %2d" % (i,j,i*j), end="\t\t")
    print("")