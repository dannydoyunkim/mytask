"""
[실습]
'data.txt'파일에서 각 라인에 회사 약어와 특정 정수값으로 이뤄져 있다. data.txt 파일의
전체 내용을 읽어 Dictionary 자료구조에 회사명을 key로 하고 정수값을 value로 하여
등록하고자 합니다. 하지만 Dictiionary 구조는 같은 key 값을 가질 수 없으므로 만약
같은 key가 존재한다면 회사명뒤에 숫자 1을 붙여 저장하려고 한다. 예를들어 naver 41이
먼저 나왔다면 Dictionary에 naver를 key로 하고 value를 41로 넣을 수 있습니다. 만약
naver 44라는 또 다른 값이 있다면 Dictionary에서 같은이름으로 들어갈 수가 없으므로
naver1이라고 key로 저장하고 value는 44로 저장하도록 하는 프로그램을 작성하시오.



<입력예>
파일 내용
lgcns  23
naver  41
google  5
hancom  61
korea  10
information  67
monitor 98
class  11
member 8
internet  2
bible  90
friends  34
forever  20
naver  44
google  55
hancom  36
korea  20



<출력예>

lgcns : 23
naver : 41
google : 5
hancom : 61
korea : 10
information : 67
monitor : 98
class : 11
member : 8
internet : 2
bible : 90
friends : 34
forever : 20
naver1 : 44
google1 : 55
hancom1 : 36
korea1 : 20

"""


def checkWord(data, dic):
    if data in dic.keys():
        return True
    return False
    

dataDic = {}

fp = open('data.txt', 'r')
dataList = fp.read().splitlines()
fp.close()

#------------------------------------------------
# 이 부분에 코딩하시오.













#---------여기까지--------------------------------------
        
for i in dataDic.keys():
    print(i, ":", dataDic[i])
    









