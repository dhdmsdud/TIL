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





