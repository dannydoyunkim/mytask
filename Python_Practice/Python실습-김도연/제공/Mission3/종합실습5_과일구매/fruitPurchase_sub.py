def fruitPurchase(dict):

    purchaseDics = {} # 추가 구입해야하는 과일이름을 key로 하고 추가 구입 갯수와
                      # 과일별 구입 소요 비용을 리스트로 만들어 value로 등록 
    total_expenses = 0 # 총 소요 비용

#------------------------------------------------
# 이 부분에 코딩하시오.

    # print(dict)
#### 내꺼
    for each_item in dict.keys() :

        fruit_expenses = 0
        fruit_cnt = 5 - dict[each_item][1] #추가 구입 개수

        if fruit_cnt > 0 :
            fruit_expenses = dict[each_item][0] * fruit_cnt # 추가 구입을 위한 비용
            purchaseDics[each_item] = list([fruit_cnt, fruit_expenses])

        total_expenses += fruit_expenses

#---------여기까지--------------------------------------

    return purchaseDics, total_expenses
    

