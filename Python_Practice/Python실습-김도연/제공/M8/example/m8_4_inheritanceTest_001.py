class Person:
    name =''
    age = 0
    gender =''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
           
    def showInfo(self):
        print("이  름 :", self.name)
        print("나  이 :", self.age)
        print("성  별 :", self.gender)
        
        
class Employee(Person):
    company =''
    department=''

    def __init__(self, name, age, gender, company, department):
        super().__init__(name, age, gender)
        self.company = company
        self.department = department

    def showInfo(self):
        super().showInfo()
        print("회사명 :", self.company)
        print("부서명 :", self.department)
        
