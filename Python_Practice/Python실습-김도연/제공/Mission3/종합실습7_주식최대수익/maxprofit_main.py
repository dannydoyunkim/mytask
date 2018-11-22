# 주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 입력: 주식 가격의 변화 값(리스트: prices)
# 출력: 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값

'''
5번째 날에 사서 8번째 날에 팔았을 때 최대 수익이 3200입니다.
4번째 날에 사서 9번째 날에 팔았을 때 최대 수익이 2800입니다.
7번째 날에 사서 11번째 날에 팔았을 때 최대 수익이 26900입니다.

'''
from maxprofit_sub import max_profit

fp = open('data1.txt', 'r')
strList = fp.read().splitlines()
fp.close()


for x in strList:
    stock = list(map(int,x.split(',')))
    res = max_profit(stock)

    print("{}번째 날에 사서 {}번째 날에 팔았을 때 최대 수익이 {}입니다.".format(res[0]+1, res[1]+1, res[2]))
