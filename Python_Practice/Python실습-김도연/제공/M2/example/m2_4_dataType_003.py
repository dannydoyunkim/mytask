#m2_4_dataType_003.py

a = 3
b = a
print("1 :", id(a)) #1578321584
print("2 :", id(3)) #1578321584
print("3 :", id(b)) #1578321584

f = 3.14
s = f
print("4 :", id(f))    #48304896
print("5 :", id(3.14)) #48304896
print("6 :", id(s))    #48304896

text = "Hello"
tmp = text
print("7 :", id(text))    #49037056
print("8 :", id("Hello")) #49037056
print("9 :", id(tmp))    #49037056


