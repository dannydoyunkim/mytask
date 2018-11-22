#일반 함수를 활용하여 전달된 두 수를 더한 값을 리턴하는 함수
def func(x, y):
    return x + y

print(func(1,2))

#함수를 변수에 대입하여 변수를 통해 함수를 호출하는 경우
v1 = func

print(v1(1,2))


#lambda 함수를 이용하여 func() 함수와 같은 기능을 할 수 있도록 한 경우
#실제 define되어 있지 않는 익명의 함수를 만드는 방법 
f = lambda x, y : x+y

print(f(1,2))


