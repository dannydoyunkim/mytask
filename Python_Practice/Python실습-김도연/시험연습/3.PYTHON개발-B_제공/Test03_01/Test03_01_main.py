'''
이 파일은 절대 수정하지 말고, Test03_01_sub.py 파일의 빈 부분을 코딩하시오
'''

from Test03_01_sub import *

if __name__=='__main__':
    carList = [ ] # 자동차 리스트

    fp = open('data03_01.txt', 'r')
    strList = fp.read().splitlines() 
    fp.close()

    lineNum = 1
    
    for  i  in  range( 0, len(strList) ) : # 1개 행씩 처리..
        carList = strList[i].split() # dataList는 자동차의 리스트를 가짐. 예) ['소형', '경차', '소형', '중형', '친환경차']

        retList = myPass(carList)  # 계산된 통행료 및 면제 대수. 예) [5000, 2]
        print('\n---- Line %d ----' % lineNum)
        print('차량 ', len(carList), '대 통행료 : ',  retList[0], '원 (면제 :', retList[1], '대)')
        lineNum += 1
