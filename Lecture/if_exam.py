# 문제 1)
# 사용자로부터 하나의 값을 입력받아(input)
# 해당 값에 20을 뺀 값을 출력하라
# 단) 출력 값의 범위는 0 ~255이다
# 예를 들어 결과값이 0보다 작은 값이되는 경우 0을 출력하고
# 255보다 큰 값이 되는 경우 255을 출력해야한다.
num = int(input("enter your number : "))
if num - 20 < 0 :
    print(0)
elif num - 20 > 255 :
    print(255)
else :
    print(num - 20)

# 문제 2)
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# 현재시간 : 02:00
# 현재시간 : 03:10
strclock = '02:00 , 03:10'
if strclock == '02:00' :
    print(True)
else :
    print(False)

# 문제 3)
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어
# 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit_list = ["사과", "포도", "홍시"]
user = input("enter your fruit : ")
if user in fruit_list :
    print("정답입니다.".format(user))
else :
    print("오답입니다.".format(user))

# 문제 4)
# 투자 경고 종목 리스트가 있을 때
# 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("enter your investment : ")
if user in warn_investment_list :
    print('투자 경고 종목입니다.'.format(user))
else :
    print('투자 경고 종목이 아닙니다.'.format(user))

# 문제 5)
# 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를
# 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
userfruit = input("enter your fruit : ")
if userfruit in fruit :
    print("정답입니다.")
else:
    print("오답입니다.")

# 문제 6)
# 사용자로부터 문자 한 개를 입력 받고,
# 소문자일 경우 대문자로,
# 대문자 일 경우, 소문자로 변경해서 출력하라.
# hint -  islower() 함수는 문자의 소문자 여부를 판별합니다.
word = input("enter your word : ")
if word.islower() :
    print(word.upper())
else :
    print(word.lower())

# 문제 7)
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 81~100 A
# 61~80	 B
# 41~60	 C
# 21~40	 D
# 0~20	 E
# 사용자로부터 score를 입력받아 학점을 출력하라.
score = int(input("enter your score : "))
if 81 <= score <= 100 :
    print("A")
else :
    if 61 <= score <=80 :
        print("B")
    else :
        if 41 <= score <= 60 :
            print("C")
        else:
            if 21 <= score <=40 :
                print("D")
            else:
                if 0 <= score <= 20 :
                    print("E")

# 문제 8)
# 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라.
# input number1: 10
# input number2: 9
# input number3: 20
num = [10,9,20]
print(max(num))

# 문제 9)
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# 휴대전화 번호 입력: 011-345-1922
usernum = input("enter your phonenumber : ").split('-')
if usernum[0] == "011" :
    print("SKT")
elif usernum[0] == "016" :
    print("KT")
elif usernum[0] == "019" :
    print("LGU")
else:
    if usernum[0] == "010" :
        print("알수없음")

# 문제 10)
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데
# 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# >> 주민등록번호: 821010-1635210
idcard = input("enter your idcard number : ")
if idcard[7] == str('1' or '3') :
    print("남자".format(idcard))
else:
    if idcard[7] == str('2' or '4') :
        print("여자".format(idcard))

# 문제 11)
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
idcard = input("enter your idcard number : ")
seoul = ['00','01','02','03','04','05','06','07','08']
busan = ['09','10','11','12']

if idcard[8:10] in seoul :
    print("출생지 : 서울".format(idcard))
else:
    if idcard[8:10] in busan:
        print("출생지 : 부산".format(idcard))

# 문제 12)
# 어떤 대학교를 졸업하려면 적어도 140학점을 이수해야
# 하고 평점이 2.0은 되어야 한 다고 하자.
# 이것을 파이썬 프로그램으로 검사해보자.
# 사용자에게 이수학점수와 평점을 물어보고 졸업 가능 여부를 출력하는 프로그램을 작성해보자.
# credits = float( input("이수한 학점을 입력하세요 : "))
# avg = float( input("평점을 입력하세요 : "))
credits = float( input("이수한 학점을 입력하세요 : "))
avg = float( input("평점을 입력하세요 : "))
if credits >= 140 and avg >= 2 :
    print("졸업가능")
else:
    print("졸업불가능")

# 문제 13)
# 1부터 10사이의 난수를 생성하고 숫자를 맞춰보자
from random import randint
answer = randint(1,5)
print(answer)


# 문제 14)
# input()함수를 이용하여 입력받은 숫자가 홀수인지 짝수인지를 판단하는 프로그램을 작성하라.
# 홀수면 '홀수'라고 출력하고 짝수면 '짝수'라고 출력하시오
# +, - , / , * , %(나머지 연산자)
inputnumber = int(input("enter your digit : "))
if inputnumber%2 == 1 :
    print("홀수")
    pass
else :
    print("짝수")