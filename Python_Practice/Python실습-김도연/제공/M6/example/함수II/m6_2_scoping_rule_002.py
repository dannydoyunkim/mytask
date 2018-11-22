def circle_area1(r):    
    pi = 3.14
    result = pi * (r ** 2)
    return result

def circle_area2(r):    
    result = pi * (r ** 2)
    return result

def sum_areas():
    results = [circle_area1(3), circle_area2(3)]
    return sum(results)       # built-in의 sum 함수를 호출


# scoping_rule2 global 영역
pi = 3.1415
print("PI:", pi)
print("반지름:", 3, "면적:", circle_area1(3))
print("반지름:", 3, "면적:", circle_area2(3))
print(sum_areas())
