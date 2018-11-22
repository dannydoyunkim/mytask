choice = None

while True:
    print("1. 원 그리기")
    print("2. 사각형 그리기")
    print("3. 선 그리기")
    
    choice = input("메뉴를 선택하시오")

    if choice == "1":
        print("원 그리기를 선택했습니다.")
    elif choice == "2":
        print("사각형 그리기를 선택했습니다.")
    elif choice == "3":
        print("선 그리기를 선택했습니다.")
        
    else:
        print("잘못된 선택을 했습니다.")
