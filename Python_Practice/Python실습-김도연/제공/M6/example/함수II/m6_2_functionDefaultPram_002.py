def circleArea(radius, pi=3.14):    
    cArea = pi * (radius ** 2)    
    return cArea    
        

radius = int(input("반지름 : "))
print("반지름:{}, 면적 :{}".format(radius, circleArea(radius)))

radius = int(input("반지름 : "))
print("반지름:{}, 면적 :{}".format(radius, circleArea(radius, 3.14)))
