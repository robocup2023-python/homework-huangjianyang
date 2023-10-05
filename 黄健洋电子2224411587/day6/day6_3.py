class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(self.name, self.age, self.gender)
class Student(Person):
    def __init__(self, name, age, gender, college, classes):
        Person.__init__(self, name, age, gender)
        self.college=college
        self.classes=classes
    def personInfo(self):
        print(self.name, self.age, self.gender, self.college, self.classes)
    def __str__(self) -> str:
        return '(Person: %s, %s, %d, %s, %s)' % (self.name, self.gender, self.age, self.college, self.classes)
hjy=Person('hjy', 19, 'man')
hjy.personInfo()
hjy=Student('hjy', 19, 'man','ele','2204')
hjy.personInfo()
print(hjy.__str__())