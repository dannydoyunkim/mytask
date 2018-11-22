ls_int = [0,0,0,0,0,0,0,0,0,0]
total = 0

for i in range(10):
    ls_int[i] = int(input("{}번째 값 :".format(i+1)))

for item in ls_int:
    total = total + item

print("1부터 10까지 합은", total, "입니다.")
