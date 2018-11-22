def circleArea(radius, pi):    
    cArea = pi * (radius ** 2)    
    return cArea    
        

radius = int(input("반지름 : "))
print("반지름:{}, 면적 :{}".format(radius, circleArea(radius, 3.14)))
