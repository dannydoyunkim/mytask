class Person:

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

        

p1 = Person("lee", 25, 175,65)
p2 = Person("kim", 20, 165,50)
p3 = Person("park", 25, 160,45)
p4 = Person("song", 33, 163,50)
p5 = Person("choi", 35, 185,70)
p1.showInfo()
p2.showInfo()
p3.showInfo()
p4.showInfo()
p5.showInfo()
