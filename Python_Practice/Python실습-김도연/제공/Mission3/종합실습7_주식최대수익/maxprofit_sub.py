def max_profit(prices):    
    max_profit = 0  # 최대 수익은 항상 0 이상의 값
    purchase_day = 0 # 주식 산 날
    sales_day = 0  # 주식 판 날
    
#------------------------------------------------
# 이 부분에 코딩하시오.

    # print(prices)
    # 최대, 최소값을 구한후 그 차액과 해당 날짜들을 기록하여 반환하면 된다 (X).
    # 주식을 산 날은 최소값일때, 주식을 판날은 최대값일때(X)
    # 주의! 단순하게 최대, 최소만 하면 안되고, 시간 순서에 따라 가야 한다.
    #       따라서, 최대 수익이 최대인 경우의 그 차액과 해당 날짜들을 기록하여 반환

    for i in range(len(prices)-1) :
        for j in range(i, len(prices)) :
            if prices[j] - prices[i] >= max_profit : # 최대값 후보
                max_profit = prices[j] - prices[i]
                sales_day = j + 1
                purchase_day = i + 1

#---------여기까지--------------------------------------   
    
    return purchase_day,sales_day,max_profit

