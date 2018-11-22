
while True :

    score = int(input("점수 입력 : "))

    if (score >= 90) :
        print("A", end='')
    elif (score >= 80) :
        print("B", end='')
    elif (score >= 70):
        print("C", end='')
    elif (score >= 60):
        print("D", end='')
    elif (score >=0) :
        print("F", end='')
    else :
        break

    if ( score >= 60 ) :
        if ( score % 10 >= 5 or score >= 100 ) :
            print("+", end='')
        else :
            print("0",end="")

    print(" 학점입니다. \n")

print("\n종료")