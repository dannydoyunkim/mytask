import random # 난수를 만드는 random 모듈 사용

correct_answer = random.randint(0, 100) # 0~100 난수 발생

count = 0

# while 무한 루프
while True :
    number = int(input("숫자를 입력하세요: "))
    if number < 0 or number > 100:
        continue
    
    count += 1
    if correct_answer == number : # 정답이면 break
        break
    elif correct_answer > number :
        print(number, "보다 큽니다!")
    else :
        print(number, "보다 작습니다!")

# 평가 출력
print("정답입니다!")
if count <= 2 :
    print(count, "번만에 맞춘 당신은 천재!")
elif count <= 4 :
    print(count, "번만에 맞추셨네요. 잘했어요^^")
else :
    print(count, "번만에 맞추다니 아쉽습니다...")
