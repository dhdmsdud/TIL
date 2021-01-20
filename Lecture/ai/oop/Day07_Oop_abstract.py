# 추상화
# 데코레이션
# 다중상속
# 제너레이터, 이터레이터
class Animal(object):
    def cry(self):
        pass

class Tiger(Animal):
    def jump(self):
        print("호랑이가 점프를 한다.")
    def cry(self):
        print("어흥")

class Lion(Animal):
    def bite(self):
        print("한 입에 꿀꺽한다.")
    def cry(self):
        print("그르렁")

class Liger(Tiger, Lion): # 다중상속
    def play(self):
        print("라이거가 사육사와 놀고있다.")

# 추상클래스
# 클래스를 만드는 이유 => 객체생성
# 추상클래스 객체생성X
# 추상메서드를 하나라도 가지면 추상클래스로 정의
# 메서드 구현을 강제하기 위해 사용
from abc import *

class Base(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    def go_to_school(self):
        print("hard study")

class Student(Base):
    def study(self):
        print("공부하자")

# 특수문법 : 데코레이션
# 함수의 인자로 다른 함수를 전달하는 과정에서 적용하 수 있는 기법
def out_function(func):
    def inner_function():
        func()
    return inner_function

def user_function():
    print("함수가 수행되었습니다.")

decorator_func = out_function(user_function)
user_function()
decorator_func()

import time
def userouterfunc(func):
    def userinnerfunc():
        print("{} 함수수행 시간을 계산합니다.".format(func,__name__))
        start = time.time()
        func()
        end = time.time() - start
        print("{} 함수수행 시간은 {} 입니다.".format(func.__name__, end))
        return userinnerfunc()
decoratoruserfunc = userouterfunc(user_function)
decoratoruserfunc()

#####
import datetime
def loggerLogin():
    print("녕이 로그인")
loggerLogin()

def datetimeDecorator(func):
    def wrapper():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return wrapper

ny = datetimeDecorator(loggerLogin)
ny()

@datetimeDecorator
def dumpfunc():
    print("함수실행")

dumpfunc()

#####
# 1. typechecker Decorator 만들기(인자의 유효성 검사)
# 2. digit01, digit02를 곱한 값을 출력하는 함수
# 3. typechecker Decorator digit01, digit02가 정수가 아니면 "only integer support"

def typechecker(func):
    def innerfunc(digit01, digit02):
        if type(digit01) != int or type(digit02) != int :
            print("only integer support")
            return # 조건처리안에서 return 실행은 함수를 종료하겠다는 의미
        return func(digit01, digit02)
    return innerfunc

@typechecker
def div(digit01, digit02):
    return digit01 * digit02

div(3, 1)

#파라미터와 관계없이 모든 함수에 적응 가능한 Decorator를 만들고 싶다면
# *args(tuple), **args(dict)
def generalDeco(func):
    def wrapper(*args, **kwargs):
        print("this is decorated")
        return func(*args, **kwargs)
    return wrapper

@generalDeco
def usersquare(digit):
    return digit * digit
print(usersquare(2))

def userplus(digit01, digit02):
    return digit01 + digit02
print(userplus(2,3))

def userquad(digit01, digit02, digit03, digit04):
    return digit01 * digit02 * digit03 * digit04
print(userquad(2,3,4,5))

#####
def makebold(func):
    def wrapper(string):
        return '<b>' + func(string) + '</b>'
    return wrapper

def makefont(func):
    def wrapper(string):
        return '<i>' + func(string) + '</i>'
    return wrapper

@makefont
@makebold
def makeboldfont(string): # 중첩된 데코를 사용하면 가장 까가운 데코가 먼저 사용됨
    return string
print(makeboldfont("두개의 데코사용"))

# class - function에도 decorator적용가능
def tagh1(func):
    def wrapper(self, *args, **kwargs): # instane의 함수를 호출할수 있게 클래스에선 self를 써야함.
        return '<h1>{}</h1>'.format(func(self, *args, **kwargs))
    return wrapper

class Per(object):
    def __init__(self, name):
        self.name = name
    @tagh1
    def getname(self):
        return self.name

per = Per("dmsdud")
print(per.getname())

# Interator
# interable 객체(interable Object)
# list, set, dict, tuple - collection
# text sequence - built-in type
# for ~ in collection :

# iterator : 순차적으로 다음데이터를 리턴 할 수 있는 객체
# 내장함수 next()를 사용해서 순환하는 다음 값을 반환
# 파이썬 모듈의 내장함수 iter()
for num in [1,2,3,4,5] :
    print(num)

for char in "text sequence" :
    print(char)

userList = [1,2,3,4,5]
print(next(userList))

userIterator = iter(userList)
print(type(userIterator), type(userList))
print(next(userIterator))

# 사용자정의 iterator 클래스
class Counter :
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return Counter_iterator(self.stop)

class Counter_iterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __next__(self):
        if self.current < self.stop :
            rtnValue = self.current
            self.current += 1
            return rtnValue
        else:
            pass
cntIterator = iter(Counter(10))
print(next(cntIterator))

# comprehension
# [출력표현식 for 요소 in sequence[if 조건식]] - list
# {출력표현식 for 요소 in sequence[if 조건식]} - set
# {key : value for 요소 in sequence[if 조건식]} - dict
dataset = [4, True, "dmsdud", 3.1, 10]
# 정수값만을 출력
inttype = [value for value in dataset if type(value) == int]
print(type(inttype), inttype)

dataset = [1,1,2,2,3,3,4,4]
settype = {value * value for value in dataset}
print(settype, type(settype))

dataset = {1 : "dmsdud", 2 : "apple", 3 : "multicampus"}
print(dataset.keys())
print(dataset.values())
print(dataset.items())
# key값이 1 이상인 데이터를 value : key로 출력
dicttype = {value : key for key, value in dataset.items() if key >= 1}
print(dicttype)
# key값을 10단위로 한번에 바꿈
dictkey = {key*10 : value for key, value in dataset.items()}
print(dictkey)

# generator : iterator를 만들어 주는 기능
# yield : 잠시 함수의 실행을 멈추고 호출한 곳에 값을 전달, 현재실행상태 유지하므로 현재 실행된 상태를 기반으로 다음코드 실행
# 메모리 성능때문에 루프를 컨트롤하기 위해 쓰임
def textSequenceFunc():
    msg = "hi dmsdud"
    for txt in msg:
        yield txt
#print(textSequenceFunc)
textSequenceFunc()

charIte = iter(textSequenceFunc())
print(type(charIte))
print(next(charIte))

charIte = iter(textSequenceFunc())
next(charIte)

def userGeneratorFunc(data):
    for tmp in data:
        yield tmp *2

twiceList = userGeneratorFunc([1,2,3,4,5])
print(type(twiceList))
# print(next(twiceList))
for t in twiceList :
    print(t)

# generator comprehension()
# lazy operation
# (출력형식 for 요소 in collection)
squaredata = (num** 2 for num in range(5))
print(type(squaredata))
print(squaredata)
print(sum(squaredata))
for data in squaredata:
    print(data, end='\t')