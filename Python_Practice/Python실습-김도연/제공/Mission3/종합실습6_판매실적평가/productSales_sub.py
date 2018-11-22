
def productSales(productList, sales_cnt, survey_grade):
    
    product_dics = {}   #파일에서 읽은 품목별 판매갯수와 평가점수를 담기 위한 dictionary
                        #품목이 key값으로 쓰이고, 판매갯수와 평가점수를 리트스로 만들어 value가 되도록 함
    
    good_products, bad_products = [], []  #우수 상품 리스트와 판매 중지 리스트
    
#------------------------------------------------
# 이 부분에 코딩하시오.

    for product_item in productList :
        # 먼저 /로 Split 해야함
        product_list = []
        product_list = product_item.split('/')

        # Key, Value 준비
        product_key = product_list[0]
        product_value = list(map(int,product_list[1:]))

        # Dictionary 담기
        product_dics[product_key] = product_value

        # 우수 상품, 판매 중지 상품 구분하여 담기
        if product_value[0] >= sales_cnt and  product_value[1] >= survey_grade :
            good_products.append(product_key)
        elif product_value[0] < sales_cnt and  product_value[1] < survey_grade :
            bad_products.append(product_key)

#---------여기까지--------------------------------------

    good_products = sorted(good_products,reverse=True) #sorted()함수를 이용하여 정렬
    bad_products= sorted(bad_products,reverse=True)    #sorted()함수를 이용하여 정렬
    return good_products, bad_products


