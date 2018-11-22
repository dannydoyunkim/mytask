#lambda를 활용하는 경우 (2)
#g(x,y)함수를 define 하지 않고 사용하는 경우

def f(g, a, b):
    return g(a,b)

print(f(lambda x,y: x*y, 20,10))
