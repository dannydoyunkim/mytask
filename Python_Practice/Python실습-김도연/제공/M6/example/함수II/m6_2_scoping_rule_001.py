def circle_area(r):
    result = 3.14 * (r ** 2)
    return result

radius = 3
area = circle_area(radius)
print("반지름: %d, 면적: %.2f" % (radius, area))
print(r)   #circle_area 함수의 지역변수를 접근하려 함
