"""
 * [실습] 제곱의 합과 합의 제곱
 * 
 * 1부터 5까지의 자연수를 각각 제곱하여 더한 것을 ‘제곱의 합’이라고 부른다.
 *    -> 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
 * 1부터 5까지의 자연수를 더한 후에 그 결과를 제곱한 것을 ‘합의 제곱’이라고 부른다.
 *    -> ( 1 + 2 + 3 + 4 + 5 )^2 = 225
 * 
 * 위의 결과에 따라, 1부터 5까지의 자연수에 대한 ‘제곱의 합‘과 ‘합의 제곱’의 차이는 225 - 55 = 170 이 된다.
 * 위와 같은 규칙이 있을 때, 1부터 주어진 숫자까지의 자연수에 대해 ‘제곱의 합’과 ‘합의 제곱’의 차이는 얼마인지 구해보자.
 * 
 * 
 * [실행 결과]
 * 
 * 1부터 5까지 자연수에 대한 결과는?
 * 170
 * 
"""


        
maxNumber = 5;      # 1부터 X까지의 자연수
result = 0;         # 결과를 저장할 변수
        
# 위의 숫자를 이용하여 제곱의 합과 합의 제곱의 차이를 구한다.        
#------------------------------------------------
# 이 부분에 코딩하시오.

sum_of_each_square = 0
square_of_sum = 0
sum = 0

for item in range(1,maxNumber+1,1) :
    sum_of_each_square += item ** 2
    sum += item

square_of_sum = sum ** 2

result = square_of_sum - sum_of_each_square

#---------여기까지--------------------------------------        

print( "1부터 %d까지 자연수에 대한 결과는?" % (maxNumber))
print( result )
 
