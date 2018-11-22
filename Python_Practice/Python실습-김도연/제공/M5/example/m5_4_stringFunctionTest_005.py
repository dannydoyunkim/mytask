s1 ='''What's new in Python 3.6\nTutorial
Library Reference\nLanguage Reference
Extending and Embedding\nPython/C API
Using Python\nPython HOWTOs\n'''

strList = s1.splitlines() ## 파일을 읽은 후에 파일의 맨 마지막 문자를 잘라낼때도 사용한다

for str in strList:
    print(str)

print("\nJoin Test")
strJoin = '*'.join(strList)
print(strJoin)
