"""
[문제]

'data.txt'파일에는 샘플 단어들이 작성되어 있다. 파일로 부터 샘플 파일을 읽고,
키보드로 포함이 되었는지 판단하고자 하는 한 문자를 입력받는다.
각 단어 중 키보드로 입력 받은 문자를 포함하고 있는 단어들만 축출하여 알파벳
순서로 정렬, 즉 사전 순서로 정렬하여 출력합니다.

<실행 예>
포함된 문자 : f
정렬전 :  ['information', 'friends', 'forever']
정렬후 :  ['forever', 'friends', 'information']

"""

from searchString_sub import checkfunc, mySort


findList =[]
n = 0

fp = open('data.txt', 'r')
strList = fp.read().splitlines()
fp.close()

findchar = input("포함된 문자 : ")

for original in strList:
   
    n = checkfunc(original, findchar)
   
    if n == True:
        findList.append(original)
        
print("정렬전 : ", findList)

mySort(findList)

print("정렬후 : ",findList)



