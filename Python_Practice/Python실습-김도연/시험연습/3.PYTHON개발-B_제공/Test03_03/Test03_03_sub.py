
def searchROOM(ROOM):

    visitPos=[]  # 방문한 좌표 튜플의 리스트  예) [ (0,0) , (0,1) , (0,2), (0,3), (3,1) ~~~~ (4,4) ]
    visitAcorn=[] # 방문한 곳의 도토리 개수 리스트 [ 1, 1, 2, 3, 1 ~~~ 1]

    #######  이 부분을  코딩하시오 ##########

    print(ROOM)

    x, y = 0, 0

    while True :
        if x > len(ROOM[0]) or y > len(ROOM) :
            break

        if ROOM[y][x] > 0 :
            visitPos.append((y,x))
            visitAcorn.append(ROOM[y][x])

        if ROOM[y][x+1] > 0 :
            x += 1
        elif ROOM[y+1][x] > 0 :
            y += 1


    print(visitPos)
    print(visitAcorn)
    print(x,y)



















    #######  여기까지  코딩하시오 ##########

    return [visitPos, visitAcorn]
