# A+ A0
# B+ B0 등으로 표시 하기

#score = 50

# 첫번쨰 방법
score = int(input("점수 : "))

# if (score >= 95) :
#     print("A+", end='')
# elif (score >= 90) :
#     print("A0", end='')
# elif (score >= 85) :
#     print("B+", end='')
# elif (score >= 80) :
#     print("B0", end='')
# elif (score >= 75):
#     print("C+", end='')
# elif (score >= 70):
#     print("C0", end='')
# elif (score >= 65):
#     print("D+", end='')
# elif (score >= 60):
#     print("D0", end='')
# else :
#     print("F", end='')
#
# print("\n종료")

# 두번때 방법
# if (score >= 90) :
#     print("A", end='')
#     if (score % 10 >= 5) :
#         print("+", end='')
#     else :
#         print("0",end="")
# elif (score >= 80) :
#     print("B", end='')
#     if (score % 10 >= 5) :
#         print("+", end='')
#     else :
#         print("0",end="")
# elif (score >= 70):
#     print("C", end='')
#     if (score % 10 >= 5) :
#         print("+", end='')
#     else :
#         print("0",end="")
# elif (score >= 60):
#     print("D", end='')
#     if (score % 10 >= 5) :
#         print("+", end='')
#     else :
#         print("0",end="")
# else :
#     print("F", end='')
#
# print("\n종료")

# 세번때 방법
if (score >= 90) :
    print("A", end='')
elif (score >= 80) :
    print("B", end='')
elif (score >= 70):
    print("C", end='')
elif (score >= 60):
    print("D", end='')
else :
    print("F", end='')

if ( score >= 60 ) :
    if ( score % 10 >= 5 or score >= 100 ) :
        print("+", end='')
    else :
        print("0",end="")

print("\n종료")