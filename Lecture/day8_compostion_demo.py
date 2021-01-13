# compositon : 상속을 피하면서 클래스의 일부 기능만을 활용
# exception :
# file 입출력
class Cal01(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y

class Cal02(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multifly(self):
        return self.x * self.y

class UserCalc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cal02 = Cal02(x, y) # 객체를 명시적으로 생성
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y
    def multifly(self):
        return self.cal02.multifly()

calc = UserCalc(3,4)
print(calc.multifly())

class UserCalc01:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.cal01 = Cal01(x, y)
    def add(self):
        return self.x + self.y
    def multifly(self):
        return self.x * self.y
    def subtract(self):
        return self.cal01.subtract()

calc01 = UserCalc01(3, 4)
print(calc01.subtract())