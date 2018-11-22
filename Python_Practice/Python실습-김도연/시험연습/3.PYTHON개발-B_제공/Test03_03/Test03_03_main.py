'''
이 파일은 절대 수정하지 말고, Test03_03_sub.py 파일의 빈 부분을 코딩하시오
'''

from Test03_03_sub import *

# 전역 변수
ROOM = []  # 방의 상태
minStep = 0 # 최소 이동 칸수

if __name__=='__main__':
    roomList = []
    
    fp = open('data03_03.txt', 'r')
    strList = fp.read().splitlines() 
    fp.close()
    # 여러 개의 방 리스트를 작성
    cnt = 0
    while True :
        if len(strList) <= 0 :
            break
        size = int(strList[0])
        strList = strList[1:]
        tmpRoom = []
        for i in range (0, size) :
            tmpRoom.append(   list(map( int, strList[0].split()))  ) #문자열--> 정수
            strList = strList[1:]
        roomList.append(tmpRoom)

    # 방의 개수 만큼 반복
    for  num  in range (0,  len(roomList)) :
        ROOM = roomList[num] # 방 배열
        print("\n\n --------  %d 회 ---------- "  % (num+1))
        print("\n방 상태")
        for m in ROOM :
            print(m)

        retList = searchROOM(ROOM) 

        # 결과를 형식에 맞춰서 출력함
        step =  len(retList[0])
        print('\n#이동 거리 : ', step)
        print("#이동 경로 : ", end = '' )
        for i in range(0, step -1) :
            print( retList[0][i], '-->', end='')
        if step != 0 :
            print(retList[0][step-1])
        else :
            print()
        print("#모은 도토리 개수: ", sum(retList[1]))
