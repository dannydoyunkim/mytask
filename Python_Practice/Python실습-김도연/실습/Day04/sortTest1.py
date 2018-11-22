num = [7,4,6,89,1,12,14,55,74,5,26,3]

### 주의. List.sort()는 원본을 변경하여 소트한다.

# num1 = sorted(num)     ## sorted( List ) 함수는 소트결과만 준다.
#
# print(num)
# print(num1)

# 그냥 만들기 ( 버블 소팅 )
# for j in range(len(num)) :
#     for i in range(1,len(num)) :
#         if(num[i-1] > num[i]) :
#             tmp = num[i-1]
#             num[i-1] = num[i]
#             num[i] = tmp


# 또는 버블 소팅이다. ( 그런데, 루프의 개수가 좀 무식하다. )
for j in range(len(num)) :
    for i in range(len(num)-1) :
        if(num[i] > num[i+1]) :
            tmp = num[i]
            num[i] = num[i+1]
            num[i+1] = tmp