#이차원 리스트 사용하기
# 학생 점수 입력하기
# 학생은 4명, 한 학생 당 4과목 수강
# 마지막에는 합계를 추가해서 넣을 것

stu = []

# 내가 쓴 오답
#score = [] 는 처음 지정할 필요가 없다. --> 틀림

for i in range(4) :
    score = []              # 초기화는 단순히 score = []
    sum_score = 0
    for j in range(4) :
        score.append (int(input("{} 학생의 {}번째 과목 점수 :".format(i+1,j+1))))
        sum_score += score[j]
    score.append(sum_score)
    stu.append(score)
    #del(score) # 이걸 쓰면 안된다. --> 틀림

print(stu)


# 정답

# for i in range(4) :
#     print("{}번째 학생 성적 입력".format(i+1))
#     tmp = []
#     for j in range(4) :
#         tmp.append(int(input("성적 입력:")))
#     stu.append(tmp)
#
# print(stu)