"""
 * [실습] Armstrong Number
 * 
 * Armstrong Number란, 임의의 어떤 수(x)와 그 수의 각 자리 수의 세제곱의 합이 같은 수를 말한다.
 *   예) x = 153 이라면, ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ) = 153 으로 같으므로, 153은 Armstrong Number 이다.
 * 
 * 100부터 999까지의 숫자 중, Armstrong Number를 구한다.
 * 
 * 
 * [실행 결과]
 * 
 * 153
 * 370
 * 371
 * 407
 * 
 """

num1 = 0   # 백의 자리 숫자 분리
num2 = 0   # 십의 자리 숫자 분리
num3 = 0   # 일의 자리 숫자 분리
result = 0 # Armstrong Number 계산 결과
      
for inx in range(100, 1000, 1):                 # 100부터 999까지 반복         
#------------------------------------------------
# 이 부분에 코딩하시오.
# 내가 한거

    # if(inx < 100 or inx > 999) :
    #     print("입력값은 100 ~ 999 사이의 값만 가능합니다.")
    #     break
    #
    # strnum = str(inx)
    #
    # num1 = int(strnum[0]) ** 3 #; print ("num1 : ", num1, end = '')
    # num2 = int(strnum[1]) ** 3 # ; print ("num2 : ", num2)
    # num3 = int(strnum[2]) ** 3 # ; print ("num3 : ", num3)
    #
    # result = num1 + num2 + num3

# 답.

    num1 = ( inx // 100 ) ** 3
    num2 = ( (inx % 100 ) // 10 ) ** 3
    num3 = ( (inx % 100 ) % 10 ) ** 3

    result = num1 + num2 + num3

#---------여기까지--------------------------------------   
            
    if(inx == result ):
        print( inx )
       
