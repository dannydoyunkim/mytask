"""
[실습]
s.split( )을 하면 이 문자열이 단어 단위로 분리된 문자열 리스트를 얻게 된다.
단어를 분리할 때 ',' 또는 '.' 등 특수 문자는 제외하고 순수 알페벳으로 구성된
문자열만 분리할 수 있도록 한다. 분리된 알파벳 리스트는 알파벳 순으로 정렬하여
출력하고 동시에 각 단어가 시용된 횟수를 출력하시오.

<출력결과>
a : 1
an : 1
and : 2
by : 1
creating : 1
development : 1
environment : 1
existing : 1
focus : 1
for : 1
in : 1
it : 2
language : 1
making : 1
materials : 1
new : 1
on : 1
possible : 1
programming : 1
propose : 1
python : 1
scripting : 1
start : 1
teach : 1
teaching : 1
to : 3
we : 1
"""


s = '''We propose to start by making it possible to teach programming
in Python, an existing scripting language, and to focus on creating a
new development environment and teaching materials for it.'''

word_list = s.lower().split()

for i in range(0,len(word_list)):
    tmp =""
    for j in range(0, len(word_list[i])):
        if(word_list[i][j].isalpha() == True):
            tmp+=word_list[i][j]
    word_list[i] = tmp

word_list.sort()   #라이브러리를 이용하여 소팅함.


#------------------------------------------------
# 이 부분에 코딩하시오.
#print(word_list)

cnt = {}

for keyword in word_list :
    if keyword not in cnt :
        cnt[keyword] = 1
    else :
        cnt[keyword] = cnt.get(keyword) + 1

#---------여기까지--------------------------------------

print()
for i in cnt.keys():
    print("{} : {}".format(i,cnt[i]))












