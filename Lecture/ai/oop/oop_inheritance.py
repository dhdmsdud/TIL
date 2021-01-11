# oop
# 상속(is ~ a), 다형성, 은닉화, 추상화
# library쓰는 법 : has ~ a , is ~ a

class Car :
    def __int__(self, name, door, cc):
        self.name = name
        self.door = door
        self.cc = cc
    def carinfo(self):
        print("%s 는 %d cc 이고, 문짝은 %d개 입니다." % (self.name, self.cc, self.door))

# Car01 = Car('GV70', 4, 2400)
# Car01.carinfo()
# Car1.함수
# Car1.변수

# class Sup(object):
#     pass
#
# class Sub(Sup):
#     pass

class Parent(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def display(self):
        return ("당신의 이름은 {} 이고, 직업은 {} 입니다.".format(self.name, self.job))

class Child01(Parent):
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
    def childinfo(self):
        print("당신의 이름은 {} 이고, 직업은 {}이며, 나이는 {} 입니다.".format(self.name, self.job, self.age))

class Child02(Parent):
    pass

class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def perinfo(self):
        return self.name + str(self.age) + self.address

# super() : 부모애 생성자를 호출
class StudentVO(Person):
    def __init__(self, name, age, address, stuid):
        super().__init__(name, age, address)
        self.stuid = stuid
    def stuinfo(self):
        return super().perinfo()+self.stuid

class TeacherVO(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject
    def teachinfo(self):
        return super().perinfo()+self.subject

class ManagerVO(Person):
    def __init__(self, name, age, address, dept):
        super().__init__(name, age, address)
        self.dept = dept
    def emptinfo(self):
        return super().perinfo()+self.dept

# encapsulation(은닉화) / information hiding(정보은닉)
class Mydate(object):
    def setYear(self, year):
        if year < 0 :
          self.__year = 2021
        else:
          self.__year = year
    def getYear(self):
        return self.__year