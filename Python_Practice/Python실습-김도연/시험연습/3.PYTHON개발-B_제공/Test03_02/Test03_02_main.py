'''
이 파일은 절대 수정하지 말고, Test03_02_sub.py 파일의 빈 부분을 코딩하시오
'''

from Test03_02_sub import *

if __name__=='__main__':
    
    inputList = []  # 파일에서 읽어온 값들의 리스트 (문자열)
    rfp = None # 입력 파일
    resList = [] # 문제 조건으로 계산한 2차원 리스트

    rfp = open('data03_02.txt' , 'r')
    line = 1
    print('**** [우수 고객 선발 결과] ****')
    while True :
        rLine = rfp.readline()
        if rLine == '' or rLine == None :
            break
        inputList= rLine.split()
        resList = selectBestCustomer(inputList)

        print('---------', line, '회----------- ')
        line += 1

        print('고객ID\t', '총구매액\t', '고객 순위')
        for customer in resList :
            print(customer[0],'\t', customer[1], '\t',customer[2])
        print()
    rfp.close()

