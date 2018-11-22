def functionVariable(v) :
    sum = 0
    cnt = 0
    
    for num in v :
        if num % 2 == 0:
            sum = sum + num
            cnt += 1
        
    return cnt, sum


cnt, sum = 0, 0

cnt, sum = functionVariable([1,2,4,5,8,10,11,12,14,15,17,18, 20])
print("1.짝수 개수 :{}, 합 :{}".format(cnt, sum))
cnt, sum = functionVariable([1, 2, 3, 4])
print("2.짝수 개수 :{}, 합 :{}".format(cnt, sum))
