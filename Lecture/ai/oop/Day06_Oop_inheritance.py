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

#####
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
    def perinfo(self):
        return super().perinfo()+self.stuid

class TeacherVO(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject
    def teachinfo(self):
        return super().perinfo()+self.subject
    def perinfo(self):
        return super().perinfo()+self.subject

class ManagerVO(Person):
    def __init__(self, name, age, address, dept):
        super().__init__(name, age, address)
        self.dept = dept
    def emptinfo(self):
        return super().perinfo()+self.dept
    def perinfo(self):
        return super().perinfo() + self.dept

# encapsulation(은닉화) / information hiding(정보은닉)
class Mydate(object):
    def setYear(self, year):
        if year < 0 :
          self.__year = 2021
        else:
          self.__year = year
    def getYear(self):
        return self.__year

# public vs private
# instance variable - public을  private으로 변경 ==> __instance variable
#instance function - public을 private으로 변경 ==> __instance variable

class HidingClass(object):
    def __init__(self, name, dept, num):
        self.utype = self.__class__.__name__
        self.name = name
        self.__dept = dept
        self.num = num
    def getDept(self):
        return self.__dept
    def __getinfo(self):
        return "__로 시작했기때문에 해당함수는 외부에서 접근불가능"

# 다형성 : 상위클래스에 정의된 함수를 하위클래스에서 해당함수를 재정의(method overriding)
# [실습]
# 1. Account class 작성 - account, balance, interestRate
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.
# 1. Account class 작성 - account, balance, interestRate, type(계좌 종류 S|F)
# 1-1. SavingAccount , FundAccount 추가
# 1-2.  |                       |
# 1.3.  -- printInterestRate()  -- printInterestRate()
# 1.4  SavingAccount - printInterestRate()
#      기본 이자율에 만기시 이자율을(0.1) 복리로 계산
# 1.5  FundAccount - printInterestRate()
#      기본 이자율에 잔액 10만원 이상이며 10%
#      기본 이자율에 잔액 50만원 이상이며 15%
#      기본 이자율에 잔액 100만원 이상이며 20%

class Account(object):
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self. interestRate = interestRate

    def accountInfo(self):
        print("계좌번호 {}, 현재잔액 {}".format(self.account, self.balance))

    def deposit(self, amount):
        self.balance -= amount

    def printInterestRate(self):
        print("%.2f" % float(self.balance + (self.balance * self.interestRate)))

    def withDraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족하여 출금할 수 없습니다")
        else:
            self.balance -= amount

class FundAccount(Account):
    def __init__(self, account, balance, interestRate, type):
        super().__init__(account, balance, interestRate)
        self.type = type

    def printInterestRate(self):
        if 0 < self.type < 100000 :
            self.balance += self.interestRate
            print(self.balance)
        elif self.balance < 500000 :
            self.balance += self.interestRate * 0.15
            print(self.balance)
        else:
            self.balance += self.interestRate * 0.2
            print(self.balance)

class SavingAccount(Account):
    def __init__(self, account, balance, interestRate, type):
     super().__init__(account, balance, interestRate)
     self.type = type

    def printInterestRate(self):
        print("%.2f") % float(self.balance + (self.balance * self.interestRate * 0.1))
