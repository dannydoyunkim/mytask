# scoping_rule3 global 영역
pi = 3.14

def circle_area(r):
    pi = pi + 0.0015
    result = pi * (r ** 2)
    return result

if __name__ == "__main__":
    print("PI:", pi)
    print("반지름:", 3, "면적:", circle_area(3))
    print("PI:", pi)
