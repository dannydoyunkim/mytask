#m2_printfunction_001.py

print(" 1: Hello LGCNS")
print(" 2:",100)
print(" 3:", 3.14)
print(" 4:%s" % ("Hello LGCNS"))
print(" 5:%c" % "H")
print(" 6:%d" % 100)
print(" 7:%o" % 10)
print(" 8:%x" % 10)
print(" 9:%f" % 10.6)

#여러가지 값의 형식이 다른 값들을 표현할 수있다.
print("10:%s %s %d등 %f%%" % ("Hello",  "LGCNS!",1,99.9))

#서식문자 %type 사이에 다양한 Flag기호와 자리수를 표현할 수 있다.
print("11:%10s%10s%2d등 %5.1f%%" % ("Hello",  "LGCNS!",1,99.9))
print("12:%-7s%7s%2d등 %5.1f%%" % ("Hello",  "LGCNS!",1,99.9))
print("13:%#o"%23)
print("14:%05d"% 23)
print("15:% d"% 23)  #숫자 앞에 공백이 추가된다.
print("16:% d"% -23)
print("17:%+d"% 23)
print("18:%+d"% -23)

