checkPattern = [(0, -1), (-1, 0), (1, 0), (0, 1)]
checkedFlag = 'o' #체크한 좌표는 다시 체크 하지 않도록 하기위해 'o'로 변경시킨다.

def checkNode(datas, x, y):    
    datas[y][x] = checkedFlag   #체크한 좌표는 다시 체크 하지 않도록 하기위해 'o'로 변경시킨다. 
#------------------------------------------------
# 이 부분에 코딩하시오.









#---------여기까지--------------------------------------   
    return False


def isPossible(data):
    # 문자열 형태인 data를 리스트로 변환
    datas = [list(line) for line in data.split("|")]

    #미로 화면 출력
    for i in datas:
        print(''.join(list(i)))
        
    # 시작지점 "S"의 위치를 찾는다.
    sX, sY = 0, 0
    
    for y in range(len(datas)):
        if "S" in datas[y]:
            sX, sY = datas[y].index("S"), y
            
    # 찾기시작          
    if not checkNode(datas, sX, sY):
        print("Not found.")



