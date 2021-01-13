# compositon : 상속을 피하면서 클래스의 일부 기능만을 활용
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

# exception : 예외를 처리할 수 있는 구문(error)
# try : 에러가 발생 할 가능성이 있는 코드
# except : 발생된 에러를 잡기위한 객체를 정의/ 프로그램의 흐름을 정성으로 컨트롤, 예외발생의 디버깅, 로그파일을 만들어 예외정보를 저장
# else : 에러가 발생되지 않을때 실행
# finally : 에러발생 유무와 상관없이 무조건 수행
# 예외가 없다고 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외처리 권장
def user_key_in():
    try:
        age = int(input("enter your age : "))
        print('예외 발생 이후 코드')
    except ValueError as e: #
        print('error = ', e)
    print('function close')

user_key_in()

# Exception사용 : 모든 예외 처리 가능
def user_key_in1():
    try:
        age = int(input("enter your age : "))
    except Exception as e:
        print("문자열이 아닌 정수형 입력")
        user_key_in1()
    else:
        print(age)
        print('function close')
    finally:
        print('happy')

user_key_in1()

#####
name_list = ['oh', "eun", "yeung"]
try:
    name = "ruby"
    idx = name_list.index(name)
except Exception as e:
    print('{} not found!!'.format(name))
else:
    print('{} found!!'.format(name, idx+1))


# 사용자 정의 예외 클래스
class Insufficient_Error(Exception):
    def __init__(self, msg):
        self.msg = msg

# raise : 클래스에 정의된 함수에 예외처리 적용 및 강제 예외 발생
class Account:
    def __init__(self, account, balance, interestrate):
        self.account = account
        self.balance = balance
        self.interestrate = interestrate
    def withdraw(self, amount):
        try:
            if self.balance < amount:
                raise Insufficient_Error('잔액부족')
        except Exception as e:
            print(str(e))
        else:
            self.balance -= amount

account = Account('100', 100000, 0.073)
account.withdraw(200000)
print('close')

# 객체생성하기 위해 클래스를 만들어야함.(변수, 함수)
# 경우에 따라 클래스 없이 객체를 생성할 수 있음.(변수)
# usage
# collections.namedtuple('클래스 이름'(변수), [변수]) -> 튜플과 리스트형식으로 만들 수 있음(원하는 문법으로 사용)
import collections
Person = collections.namedtuple('Person', ['name', 'id']) # 리스트형식
per = Person('RUBY', '100')
print(per, type(per))

Person = collections.namedtuple('Person', 'name id') # 튜플형식
per = Person('RUBY', '100')
print(per, type(per))

Person = collections.namedtuple('Person', 'name, id') # 스트링형식
per = Person('RUBY', '100')
print(per, type(per))

# 속성에 접근1.
print(per[0])
print(per[1])
for idx in range(len(per)):
    print('idx {} - {}'.format(idx, per[idx]))

# 속성의 접근 2.
print(per.name)
print(per.id)

# 속성의 접근 3.
(name,id) = per
print(name, id)

# 직장인 이름, 나이, 부서를 속성으로 갖는 클래스 만들기
# 직장인 이름, 나이, 부서를 속성으로 갖는 클래스를 named tuple로 만들기
class Office(object):
    def __init__(self, name, age, room):
        self.name = name
        self.age = age
        self.room = room

import collections
emp = collections.namedtuple('Office', ['name', 'age', 'room'])
emp01 = emp('ruby', 25, 'happy')
print(emp01.name, emp01.age, emp01.room)