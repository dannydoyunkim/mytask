"""
 * 특정 파일에서 내용을 읽어 분석하는 경우의 예를 작성하였습니다.
   다음과 같은 문제가 주어진 경우 접근하는 절차 (1)

   파일의 형식은 모든 라인이 같으므로 임의의 한 줄을 문자열로 생각하고
   필요한 로직을 생각합니다.
   필요한 HTTP 상태값이 200  400  401 등 서로 다른 값이지만 위치는 같기 때문에
   HTTP 상태값의 위치와 URL위치를 찾아야 합니다.
   다음과 같은 코드를 통해 제공된 샘플 파일 중 임의의 한 줄을 어떤 기준으로 나눌 지
   생각하고 split()를 통해 각 위치값을 알아봅니다.
 * 

"""


tmp = '64.242.88.10 - - [07/Mar/2004:19:41:33 -0800] "GET /twiki/bin/edit/Main/Header_address_token_limit?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846'
#tmp1='64.242.88.10 - - [07/Mar/2004:19:56:41 -0800] "GET /twiki/bin/rdiff/Main/WebIndex HTTP/1.1" 200 46373'
tmp1='h24-71-249-14.ca.shawcable.net - - [07/Mar/2004:22:29:13 -0800] "GET /icons/mailman.jpg HTTP/1.1" 200 2022'


res = tmp1.split()
print(res)



for i in range(len(res)):
    print("res[%d] = %s"%(i, res[i]))
    
