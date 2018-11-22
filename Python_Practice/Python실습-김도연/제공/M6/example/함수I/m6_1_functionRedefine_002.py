def plus(num1, num2) : 
      sum = num1 + num2
      return sum

def plus(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum

myList1 = [1,2,3]
myList2 = [6,7,8]
myList3 = [9,10,15]

mytuple1 = (1,2,3)
mytuple2 = (6,7,8)
mytuple3 = (9,10,15)

result = plus(10,20,30)
print("1 :", result)
result = plus(1.5, 3.1, 7.0)
print("2 :", result)
result = plus("Hello ","LGCNS!", "Fighting")
print("3 :", result)
result = plus(myList1, myList2, myList3)
print("4 :", result)
result = plus(mytuple1, mytuple2, mytuple3)
print("5 :", result)


