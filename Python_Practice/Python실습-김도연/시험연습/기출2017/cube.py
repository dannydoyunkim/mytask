cube = [[5,7,8],
        [4,2,1],
        [2,5,6]]

## 먼저 규칙을 찾자
# cube = [[5,7,8],
#         [4,2,1],
#         [2,5,6]]
#
# # 위의 큐브를 시계방향으로 90도 회전하여 데이터를 담고,
# # 두개를 합해야 한다.
# # cube1 = [[2,4,5],
# #         [5,2,7]
# #         [6,1,8]]
#  1) [0][0] -> [0][2]
#     [0][1] -> [1][2]
#     [0][2] -> [2][2]
#  2) [1][0] -> [0][1]
#     [1][1] -> [1][1]
#     [1][2] -> [2][1]
#  3) [2][0] -> [0][0]
#     [2][1] -> [1][0]
#     [2][2] -> [2][0]


# 정답은 아래와 같다.
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for inx in range(len(cube)) :
    for jnx in range(len(cube[inx])) :
        result[jnx][inx] = cube[jnx][inx] + cube[len(cube)-inx-1][jnx];

# 출력하기
for i in range(len(result)) :
    for j in range(len(result[i])) :
        print(result[i][j], end ="\t")
    print("")

######### 하기는 전부 틀렸다. 90 도 회전이다.
# def next_location(x,y,max_x,max_y) :
#
#     if x == max_x :
#         if y <= max_y :
#             y += 1
#         elif y >= 0 :
#             y -= 1
#     elif x < max_x :
#         x += 1
#     elif x == 0 :
#         if y <= max_y :
#             y += 1
#         elif y >= 0 :
#             y -= 1
#
#
#
#
#     if x <= max_x :
#
#     elif x <= 0 :
#         if
#
#
#
# cube = [[5,7,8],
#         [4,2,1],
#         [2,5,6]]
#
# # 위의 큐브를 시계방향으로 90도 회전하여 데이터를 담고,
# # 두개를 합해야 한다.
# # cube = [[5,7,8],
# #         [4,2,1],
# #         [2,5,6]]
#
# # 0 5 7 8 0 -> 0 0 5 7 8
# # 0 4 2 1 0 -> 0 4 2 8 1
# #
# # 0 2 5 6 0 -> 2 5 6 1 0
# # 2 5 6 1 0 -> 0 5 6 1 0   2 가 남는다
# #
# #
# # 0 4 2 8 1 -> 0 2 2 8 0   4 가 남는다
# # 0 4 5 7 8 -> 0 4 5 7 0
#
# # 복잡하게 생각하지 말고 Cusor의 위치를 변경하면서 새로 만들자
# # 최초 커서의 위치는 x=1, y=0
# # max_x = 2, max_y = 2 이다
# # x가 max_x에 도달하면 y가 증가한다
# # y가 max_y에 도달하면 x는 감소한다
# # x가 0에 도달하면 y가 감소한다
# # y가 0에 도달하면 종료된다.
# # 만일, 해당 위치의 값이 0이 아니면, 다음으로 진행하고, x = 1, y = 1에서 끝난다.
# # 이동은
#
#
# cube1 = [[0,0,0][0,0,0][0,0,0]]
#
# o_x,o_y = 1,0
# n_x,n_y = 2,0
# max_x, max_y = len(cube[0]), len(cube[0])
#
# for i in range(len(cube[0])**2) : # Cube의 빈칸은 정방이므로 가로길이의 제곱이다. (Loop 횟수)
#
#     if cube1[n_x][n_y] == 0 :           # 값이 비어 있으면 일단 입력하기
#        cube1[n_x][n_y] = cube[o_x][o_y]
#     else :                             # 값이 모두 있으면 Loop를 빠져 나간다. (다했으니까)
#        break
#
#     # x,y 좌표값이동
#     # 다음 좌표 구하는 함수 만들자





