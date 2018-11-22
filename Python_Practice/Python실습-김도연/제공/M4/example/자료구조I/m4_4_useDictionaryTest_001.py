myDict1 = {}
myDict2 = dict()

myDict1["park"] = "Seoul"
myDict1["choi"] = "Deagu"

myDict2["park"] = "Busan"
myDict2["choi"] = "Deajeon"

# 키가 같으면 덮어쓰기가 된다.
myDict2["park"] = "Seoul"
myDict2["choi"] = "Deagu"

print("park : ", myDict1["park"])
print("choi : ", myDict1["choi"])
print("park : ", myDict2["park"])
print("choi : ", myDict2["choi"])

# 추가적인 명령어

if "park" not in myDict1 :
    myDict1["park"] = "test"

print("park : ", myDict1["park"])
print("choi : ", myDict1["choi"])
print("park : ", myDict2["park"])
print("choi : ", myDict2["choi"])