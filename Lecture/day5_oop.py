# python 객체지향 프로그래밍 (oop) : object oriented programming
# 패키지>모듈>클래스>함수
# real world                 추상화                 program world
# object                     class                   instance
# 명사적 특징                   변수
# 동사적 특징                   함수
# class vs instance 차이점 인지
# namespace : 객체를 인스턴스화 할때 저장되는 공간
# class variable : 직접 접근가능 및 공유
# instance variable : 객체소유로 별도로 존재
# self : instance 소유임을 명시
# class : 함수의 모임 , 여러개의 함수와 데이터를 묶어 객체생성 가능한 템플릿
# 변수(데이터) + 매서드(함수) / 생성자(초기화)
# class 클래스이름 :
#     변수            -자료저장
#     초기화          -객제저장시 호출되는 함수
#     def 함수이름() : -자료처리
# use define function (-set , -get , -is)
class Calc :
    x = 0
    y = 0
    def __init__(self):
        print("객체생성시 호출되는 함수고 내 이름은 초기화야")
    def plus(self):
        print("사용자정의 함수고 난 인스턴트의 소유야")

# instance 생성하는 문법
obj = Calc()
obj.plus()

# 학생들의 정보
class Student :
    scholarshiprate = 3.5 # class variable(클래스소유)

    def __init__(self , name , major, num , grade):
        self.name = name
        self.major = major
        self.num = num
        self.grade = grade
    def __repr__(self):
        return self.name+self.major+self.num+str(self.grade)
    def getInfo(self):
        return "이름 : {} 전공 : {}".format(self.name , self.major)
    def isScholarship(self):
        if str(self.grade) >= self.scholarshiprate:
            return True
        else:
            return False
stu01 = Student("녕" , "식영" , "2017" , "4.5")
print(stu01.isScholarship() , Student.scholarshiprate)


stulist = []
stulist.append(Student("녕","식영",'2017','4.5'))
for stu in stulist :
    print(stu)

# 인스턴트 소유가 아닌 class method
# self x
# class 함수 : cls인자를 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조하기 위해 사용됨.
class Employee :
    raiseRate = 1.1 # 급여인상료 class variable
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return "현재{}님의 급여는 {}입니다.".format(self.name,self.salary)
    @classmethod
    def updaterate(cls,rate):
        cls.raiseRate = rate
        print("인상률이 {}로 변경됨".format(rate))

    def applyRaise(self):
        self.salary = int(self.salary * Employee.raiseRate)

   # static 함수
    @staticmethod
    def isvalid(salary):
        if salary < 0
            print("음수x")

emp01 = Employee("녕" , "1000")
print("인상 전 급여 - " , emp01.getSalary())

Employee.updaterate(1.5)
emp01.applyRaise()
print("인상 후 급여 - " , emp01.getSalary())

Employee.isvalid()






