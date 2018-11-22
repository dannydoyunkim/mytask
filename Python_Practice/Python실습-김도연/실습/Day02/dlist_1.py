#이차원 리스트 사용하기

list1 = [1,2,3,4]
list2 = [7,5,6,7]
list3 = [1,8,9,10]

dlist = [[1,2,3,4],[7,5,6,7],[1,8,9,10]]

# 하기와 같이 할 수 있다.
for i in dlist[0] :
    print(i, end=' ')

for i in dlist[1] :
    print(i, end=' ')

for i in dlist[2] :
    print(i, end=' ')

# 하지만 nestedloop를 쓰면 하기 처럼 간단히 쓸 수 있다. 이는 하나씩 수정은 못한다.
for j in dlist : # j는 dlist[0], dlist[1] 등을 가져오게 되고
    for i in j : # i는 dlist[0][0]부터 하나씩 가져오게 된다.
        print(i, end=' ')

#### 같은 코드는 하기 처럼 쓸수 있다 --> 이거는 하나의 값을 가지고 수정하면서 할 경우는 유용하다.
for j in range(len(dlist)) :
    for i in range(len(dlist[j])) :
        print(dlist[j][i], end=' ')

