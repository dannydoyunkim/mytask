tmp =["park","lee","hong","song","kim","lee","choi"]

# 또는 버블 소팅이다. ( 그런데, 루프의 개수가 좀 무식하다. )
# 문자열도 그냥 비교하면 된다.
for j in range(len(tmp)) :
    for i in range(len(tmp)-1) :
        if(tmp[i] > tmp[i+1]) :
            temp = tmp[i]
            tmp[i] = tmp[i+1]
            tmp[i+1] = temp

## 회수를 좀 줄이려면 아래처럼 맨 뒤에 정렬된 것은 생략하면 된다.
for j in range(len(tmp)) :
    for i in range(len(tmp)-1  -j) :
        if(tmp[i] > tmp[i+1]) :
            temp = tmp[i]
            tmp[i] = tmp[i+1]
            tmp[i+1] = temp

print(tmp)