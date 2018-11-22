"""
 * [실습] 시저의 암호
 * 
 * 여러 가지 암호문 중에서 '시저의 암호'는 알파벳을 3자씩 건너 띄어 사용한다. 즉,
 *   A -> D
 *   B -> E
 *   ...
 *   Y -> B
 *   Z -> C
 * 와 같이 바꾸어 쓰는 것이다. 이렇게 하면 THEY 가 WKHB 로 바뀌게 된다.
 * 주어진 영어 문장을 시저의 암호로 바꾸도록 한다.
 * 입력 받는 영어 문장은 대소문자를모두 받을 수 있지만, 시저의 암호에서는 모든 문자를 소문자로 취급한다.
 * 
 * 
 * [실행 결과]
 * (1) ZxyHello 실행한 경우
 * ZxyHello -> cabkhoor
 
 * (2) HelloWorld 실행한 경우
 * HelloWorld -> khoorzruog
 * 
"""

original = "ZxyHello";
#original = "HelloWorld";
result = "";    # 암호화된 문자열 결과 저장

#시저의 암호 방식으로 주어진 영어 문장을 변경해 보자.
#------------------------------------------------
# 이 부분에 코딩하시오.

# 문자열을 소문자로 변환 .lower() / 대문자로 변환 .upper()

# 내가 한거
# for each_char in original.lower() :
#     result = result + chr(ord("a")+(ord(each_char)-ord("a")+3)%(ord("z")-ord("a")+1))
#     # a-z 까지의 전체 길이로 나우었을때 나머지를 a에 더하면 된다.
#     # ord ("A") -> Ascii로 변환, chr(65) -> 문자로 변환


# ------------ 정답 ----------

for i in original :
    tmp1 = i.lower()

    if tmp1 >= "x" and tmp1 <= "z" :
        tmp = chr(ord(tmp1)-23)
    else :
        tmp = chr(ord(tmp1)+3)

    result += tmp


#---------여기까지--------------------------------------   
print( original + " -> " + result );
