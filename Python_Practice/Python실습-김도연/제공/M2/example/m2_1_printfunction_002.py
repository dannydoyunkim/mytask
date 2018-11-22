#m2_printfunction_002.py

print(" 1:{}".format("Hello LGCNS"))
print(" 2:{}".format("H"))
print(" 3:{}".format(True))
print(" 4:{}".format(10))
print(" 5:{}".format(10.6))
print(" 6:{}".format([2,3,5,1]))
print(" 7:{}".format((2,3,5,1)))
print(" 8:{}".format({2,3,5,1,2,4,1,5,2,3,4,8,9,1}))
print(" 9:{}".format({'a':2,'b':3,'c':5}))

#여러가지 값의 형식이 다른 값들을 표현할 수있다.
print("10:{0} {1} {2}등 {3}%%".format("Hello",  "LGCNS!",1,99.9))

#{:option}의 option 부분에 다양한 기호와 자리수를 표현할 수 있다.
print("11:{0:<7s}{1:7s}{2:2d}등 {3:5.1f}%%".format("Hello","LGCNS!",1,99.9))

#{}내에 인덱스 번호는 생략 가능하다.
print("12:{:7s}{:7s}{:2d}등 {:5.1f}%%".format("Hello",  "LGCNS!",1,99.9))


