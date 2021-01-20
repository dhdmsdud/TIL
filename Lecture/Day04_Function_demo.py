# python function
# 함수는 가독성을 높이기 위한 방법으로 하나 이상의 본문을 가지고 있는 코드를 정의
# 내장함수 : 사용자정의함수
# def
# user define function
def userprint( ) :
    print('userprint')

# from digital.python import package_function
# package_function.printcoins()
# from digital.python import package_function as f
# f.printcoins()
# from digital.python.package_function import printcoins
# printcoins()

from digital.python import package_function as f
rtnmsg = f.returnfunc()
print("call returnfunc() - " , rtnmsg)

echomsg = f.sayecho('녕')
print("call sayecho() - " , echomsg)

domain = f.makeurl('naver')
print("call domain() - " , domain)

tuprtn = f.tuplefunc(1,2,3,4,5,6,7,8,9)
print("call tuplefunc() - " , tuprtn)

f.dictfunc(name='dmsdud', gender='w')

(oddsum, evensum) = f.cntsum(100,500)
print("홀수합{}, 짝수합{}".format(oddsum , evensum))

# 인자로 넘겨받은 년도 사이의 윤년을 찾아 리턴시켜주는 함수작성
# list type
leapyearlist = f.leapyearfunc(1900, 2021)
print("leapyearlist - " , leapyearlist)

dictmsg = f.rtndictfunc(10)
print('dictmsg-' , type(dictmsg) , dictmsg)
for value in dictmsg.values() :
    print('dictvalues - ' , value)

# default parameter 사용 => z가 없어도 true라고 정의
# worker
def defaultparam(x,y,z = True) :
    paransum = x + y
    if paransum > 10 and z :
        return paransum
    else :
        return 0
# caller
result = defaultparam(10,20)
print("caller defaultparam()" , result)

# 함수의 입력인자 : list , dict ==> mutable
# 함수의 입력인자 : 숫자 , 문자 , tuple ==> immutable
tmplist=[10]
tmpx = 10
def mutablefunc(arglist , argx) :
    arglist.append(100)
    argx = argx + 100

mutablefunc(tmplist , tmpx)
print("tmplist-" , tmplist , type(tmplist))
print("tmpx-" , tmpx)

# variable(변수) : 선언위치에 따라(local , global)
tmp = 100
def myfunc(x) :
    global tmp
    tmp += x
    return tmp
print(myfunc(100))

#####
def personinfo(weight, height, **other):
    print(weight ,  height, other, type(other))

personinfo(54, 184, name='녕', adress='anyang')

#####
def overroll(args1, args2,*args3,**args4) :
    print(args1,args2,args3,args4)

overroll(10,20,"lee","kim","park","cho",age1=20,age2=30,age3=40)

# nested function (중첩함수)
# innerfunc는 호출불가
# outerfunc : 자료생성 , innerfunc포함
# innerfunc : 자료 연산/처리(합,평균)
def outerfunc(num) :
    def innerfunc(num) :
        print("innerfunc-" , num)
    innerfunc(num+100)

outerfunc(100)

def calfunc(data) :
    dataset = data
    def sumfunc():
        total = sum(dataset)
        return total
    def avgfunc(total):
        avg = total / len(dataset)
        return avg
    return sumfunc , avgfunc

data = list(range(1,101))
print("range date" , data)

rtnsumfunc , rtnavgfunc = calfunc(data)
tot = rtnsumfunc()
print(tot)
avg = rtnavgfunc(tot)
print(avg)

# self recursive function : 재귀함수
# 함수 내부에서 자신의 함수를 반복호출하는 기법
# 반복적으로 변수를 변경해서 연산할때 사용 (누적, 팩토리얼)
def countfunct(n): # n=5->1,2,3,4,5
    if n == 0 :
        return  0
    else:
        countfunct(n-1)
        print(n, end="")
countfunct(5)

# 누적 : (n)=1+2+3+4+....+n
def addsum(n) :
    if n ==1 :
        return 1
    else:
        result = n + addsum(n-1)
        return result

print("n=5 " , addsum(5))
print("n=100" , addsum(100))

# 익명의 함수를 만드는 방법 : (lambda)
# 가독성 향상, 코드간결, 메모리절약(즉시실행 함수)
def multifunc(x,y) :
    return x * y
print(multifunc(10, 50))

# syntax : lambda arg : body
lambdavar = lambda x,y : x*y
print(lambdavar(10,50))

def lambdafunc(x,y,func):
    print("lambdafunc-" , x*y*func(100,100))
lambdafunc(10,20,lambda x,y : x*y)

# hint
def totalfunc(word: str , num : int) :
    return len(word) * num
print("hint-" , totalfunc("dmsdud",10))












