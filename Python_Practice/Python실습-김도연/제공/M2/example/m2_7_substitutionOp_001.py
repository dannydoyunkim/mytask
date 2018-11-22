#m2_substitutionOp_001.py

x = 15      #대입연산자 

x = x + 1
print("1 :", x)

x += 1     #x = x + 1의 복합대입연산자
print("2 :",x)

y = 10    #대입연산자
y *= x    #y = y * x의 복합대입연산자
print("3 :",y)

x-=3      #x = x - 3의 복합대입연산자
print("4 :",x)
x/=2      #x = x / 4의 복합대입연산자
print("5 :",x)
x//=3     #x = x // 4의 복합대입연산자
print("6 :",x)
x%=3      #x = x % 4의 복합대입연산자
print("7 :",x)
x**=5     #x = x ** 5의 복합대입연산자
print("8 :",x)
