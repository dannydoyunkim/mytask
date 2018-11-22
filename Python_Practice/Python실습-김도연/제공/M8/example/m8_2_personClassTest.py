class Person:  ##### 클래스 다  ===== 객체를 위한 틀 이다
    name =''
    age =0
    height = 0  #cm 단위
    weight = 0  #kg 단위

    def showinfo(self):
        print("이  름 :", self.name)
        print("나  이 :", self.age)
        print("몸무게 :", self.weight)
        print("키(Cm) :", self.height)

p1 = Person()

p1.name = 'Hong'
p1.age = 30
p1.height = 170
p1.weight = 60

p1.showinfo()