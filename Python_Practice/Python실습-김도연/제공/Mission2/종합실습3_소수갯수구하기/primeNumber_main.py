"""
 * [문제] 소수 개수 구하기
 * 
 *
 * 제공된 data.txt 파일에는 각 라인별로 시작 값과 끝 값을 1 10 과 같은 형식으로
 * 적혀 있습니다. 1부터 10사이에 존재하는 모두 소수를 찾아서 그 리스트를 출력하고
 * 주어진 구간내의 전체 소수 개수를 구하는 프로그램을 작성합니다.
 *
 * 소수(Prime Number)란?
 *   1과 자기 자신을 제외한 숫자로 나누어 떨어지지 않는 숫자를 말한다.
 *      ex) x = 23 이라면, 23은 1과 23으로만 나누어 떨어지므로, 소수이다.
 *
 * <실행결과>
   < 1 ~ 10 사이의 소수 리스트는 총 4 개 입니다.>
     2 3 5 7 
   < 10 ~ 30 사이의 소수 리스트 총 6 개 입니다.>
     11 13 17 19 23 29 
   < 20 ~ 100 사이의 소수 리스트 총 17 개 입니다.>
     23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
 * 
"""

from primeNumber_sub import primeNumber

fp = open('data.txt', 'r')
strList = fp.read().splitlines()
fp.close()

for data in strList:     

     resList = primeNumber(data)
     
     print("<",resList[0],"~", resList[1],"사이의 소수 리스트는 총", resList[len(resList)-1],"개 입니다.>")
           
     for pn in range(2,len(resList)-1):
          print("{} ".format(resList[pn]), end='')
     print()


