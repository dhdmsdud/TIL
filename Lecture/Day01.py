# 변수선언 방법 3가지
# camel case: 함수정의시 많이 사용 =numberOfCollageGraduates
# pascal case: 클래스 정의시 =NumberOfCollageGraduates
# snake case: number_of_collage_graduates


a = 100
print(a)
#del a : a의 정의를 지움


# 파이썬의 데이터 타입 (built-in types)
# numeric : 정수,실수
# sequence : list, tuple, range
# text sequence : str
# mapping : dict
# set : set (중복과 순서가 정의되지 않음)
# bool : true(t), false(f), not, and, or(논리연산자) / , &,: ~(비교연산자)
# date, timedate : 날짜


# numeric(숫자, 정수, 실수)
a = 123
b = 3.14
c = 3.14E10 #==> 지수
e = 0o34 #==> 8진수
f = 0xab #==> 16진수

#type() ==> 어떤 형태의 타입인지 알아볼때 사용
print(type(a))

div = 3/4 #==> 나누기
print(div)

result = 10//3 #==> 몫
print(result)

result = 3**3 #==> 자승
print(result)

result = 10 % 3 #==> 나머지 값
print(result)


# list 생성방법
a =[]
print(type(a))
a =list()
print(type(a))

a = [1,2,3]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[-3]) #==>-1을 한 값
print(a[-2])
print(a[-1])


# seperator
a = 'apple'
b = 'banana'
c = 'melon'
print(a, b, c, sep='!')
print(a, b, b, c, sep='/n')
#참고 : Escape 코드
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \000 : 널 문자


# end
print('welcome to' , end='')
print('it news' , end='')
print('web sites' , end='')


# slicing
print('slicing')
print(a[0:2]) #==> 0번째부터 2번재까지 보여줘 (마지막에서 -1)
print(a[0:1])


# format
one = 1
two = 2
print(one, two)
print('%d,%d' % (one, two))
print('{},{}'.format(one, two))


# tuple
a = tuple()
print(type(a))
a = (1,2,3)
print(a[0])