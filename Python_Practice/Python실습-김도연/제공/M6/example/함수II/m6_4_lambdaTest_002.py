#lambda를 활용하는 경우 (1)
#g(x,y) 함수를 define 하였을 경우
def g(x,y):
    return x*y

f = lambda g, a, b :g(a,b)

print(f(g, 20,10))
print(f(g,30,40))
