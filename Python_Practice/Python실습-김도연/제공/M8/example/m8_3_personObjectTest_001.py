class Person:
    name =''
    age =0
    height = 0  #cm 단위
    weight = 0  #kg 단위

    def setAge(self, age):
        self.age = age

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def showInfo(self):
        print("이  름 :", self.name)
        print("나  이 :", self.age)
        print("몸무게 :", self.weight)
        print("키(Cm) :", self.height)


print("\n객체 생성 후 속성값 확인")        
p1 = Person()
p1.showInfo()

print("\n클래스 멤버 변수 값 설정 후 확인")
p1.name = "hong"
p1.setAge(20)
p1.setHeight(170)
p1.setWeight(72)
p1.showInfo()
