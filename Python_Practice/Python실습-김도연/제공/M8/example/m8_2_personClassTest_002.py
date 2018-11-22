class Person:
    name =''
    age =0
    height = 0  #cm 단위
    weight = 0  #kg 단위

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

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

        
