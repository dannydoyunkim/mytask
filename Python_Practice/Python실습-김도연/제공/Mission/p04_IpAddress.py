"""
 * [실습] IP 주소 알아보기
 * 
 * 32bit의 IP 주소를 입력으로 받아 8자리씩 끊어서 10진수로 바꾸어 출력해 보자.
 * 공백 없이 이진수 32자리 숫자를 입력으로 받아서 우리가 아는 형태의 IP주소인
 * 10진수.10진수.10진수.10진수 로 출력한다.
 * 
 * 
 * [실행 결과]
 * 
 * 11001011100001001110010110000000
 * IP 주소 : 203.132.229.128
 * 
"""

        
binaryIp = "11001011100001001110010110000000"
#binaryIp = "11001011 10000100 11100101 10000000"
resultIp = "" # IP주소 변환값 저장 결과
        
        
# 2진수 형태의 IP 주소를 10진수 형태의 IP 주소로 변환한다.
        
#------------------------------------------------
# 이 부분에 코딩하시오.

# ------------- 방법 1
# each_byte = 0
# each_bit = ""
#
# for ipLen in range(0,len(binaryIp),8) :
#     # 8 bit씩 잘라서, 10진수로 변환하는 로직
#     for split_byte in range(0,8) :
#         each_bit += binaryIp[split_byte+ipLen] #;print(each_bit)
#     each_byte = int(each_bit,2);
#
#     # 10진수로 분리하고, 마지막 .을 제외시키는 로직
#     resultIp = resultIp + str(each_byte)
#     if(ipLen != 24 ) :
#         resultIp += ".";
#
#     # 각 8bit 추출후 초기화하는 로직
#     each_bit=""


# ------------ 방법 2
# byte_char = ""
#
# for each_bit_char in binaryIp :
#
#     byte_char = byte_char + each_bit_char
#
#     if(len(byte_char) == 8) : #8bit가 모이면 변환
#         resultIp += str(int(byte_char, 2))
#         if(len(resultIp) < 3*(len(binaryIp)/8+1)) : # 10진수로 변환시 최대 길이 (8 bit씩의 개수 + . 개수 )* 3
#             resultIp += '.'
#         byte_char = ""
#
# print("")

# --------- 답
ip1 = binaryIp[0:8]  # index가 0부터 8-1까지를 말한다
ip2 = binaryIp[8:16]
ip3 = binaryIp[16:24]
ip4 = binaryIp[24:32]

resultIp = str(int(ip1,2)) + "." + str(int(ip2,2)) + "." + str(int(ip3,2)) + "." + str(int(ip4,2))

#---------여기까지--------------------------------------   

print( binaryIp )
print( "IP 주소 : " + resultIp )




















