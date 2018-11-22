def snailNumber(array, r, c):

    lst = list()

    cnt = 0         # 현재 출력할 수
    curr_point = (0,0)  # 현재 수를 출력할 좌표
    curr_direct = 'RIGHT'   # 현재 방향

    # 방향을 넣으면 움직여야할 좌표를 반환하는 dictionary
    # 이차원 리스트에서 움직일 수있는 방향은 상하좌우 4개의 방향
    move = {'UP': (-1,0),'DOWN': (1,0),'LEFT': (0,-1),'RIGHT': (0,1)}

    # 현재 방향을 넣으면 다음방향을 반환하는 dictionary
    next_direct = {'UP': 'RIGHT','RIGHT': 'DOWN','DOWN': 'LEFT','LEFT': 'UP'}

    # 방향이 바뀔때 마다 움직여야할 거리를 순서대로 list에 담음
    for i in range(r+c-1):  
        if i % 2 is 0:
            lst.append(c)
            r = r - 1            
        else:
            lst.append(r)
            c = c - 1
            
           
 # array에 차례로 숫자를 씀
#------------------------------------------------
# 이 부분에 코딩하시오.









#---------여기까지--------------------------------------   
        
