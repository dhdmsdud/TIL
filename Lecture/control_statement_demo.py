# control statement
# if(조건문) , for(반복문) , while(반복문)

# 사용자 입력함수
# input()
name = input("enter your name : ")
grade = input("enter your grade : ")
company = input("enter your campany : ")
print(name,grade,company)

# 짝수인지 홀수인지를 판별
# if , if ~ else , if ~ elif ~ else
# bool True | False
inputnumber = int(input("enter your digit(1 ~ 100) : "))
print(inputnumber%2 == 0)

if inputnumber%2 == 1 :
    print("짝수")
    pass
else :
    print("홀수")

# 3의 배수인지 5의 배수인지 판별
number = 15
if number%3 == 0 | number%5 == 0 :
    print('{}은 3과 5의 배수다'.format(number))
else :
    print('{}은 3과 5의 배수가 아니다'.format(number))

# if ~ elif
if number%3 == 0 :
    print('{}은 3의 배수다'.format(number))
elif number%5 == 0 :
    print('{}은 5의 배수이다.'.format(number))
    pass
else :
    print('{}은 3과 5의배수가 아니다.'.format(number))

# 윤년의 조건
# 4의 배수이고 100의 배수가 아니거나 400의 배수
# if구문을 사용하여 년도와 월을 압력받아서 월의 마지막 일을 출력한다면?
year = 2021
if (year%4 == 0 and year%100 != 0) or (year%400 == 0 ) :
    print('{}는 윤년이다.'.format(year))
    pass
else :
    print('{}는 윤년이 아니다.'.format(year))

year = int(input('년도를 입력 : '))
month = int(input('달을 입력 : '))

year_month      = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31]

if (year%4 == 0 and year%100 != 0)  :
    print('{}년 {}월의 마지막 일은 {} 입니다.'.format(year , month , leap_year_month[month-1]))
    pass
elif (year%400 == 0 ) :
    print('{}년 {}월의 마지막 일은 {} 입니다.'.format(year, month, leap_year_month[month - 1]))
else :
    print('{}년 {}월의 마지막 일은 {} 입니다.'.format(year, month, leap_year_month[month - 1]))

# list를 이용한 if ~ in
area = ['서울','부산','제주','광주']
region = '수원'
if region in area :
    pass
else :
    print('{} 지역은 포함안됨'.format(region))

# dict를 이용한 if ~ in
areakey = {'서울' : 100 , '광주' : 200}
region = '부산'
if region in areakey :
    pass
else :
    print('{} 값 존재하지 않음'.format(region))

# 삼항 연산자
num = 9
result = 0
result = num * 2 if num > 5 else num + 2
print(result)
