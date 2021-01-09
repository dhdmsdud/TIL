# 전달값과  반환값
def open_account(): # 계좌개설
    print("new account")
open_account()

def deposit(balance, money): # 입금
    print("입금완료.{}원".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money :
        print("출금완료. 잔액은{}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금불가. 잔액은{}원 입니다.".format(balance))
        return balance

def night_withdtaw(balance, money): # 수수료포함 출금
    commission = 100 #수수료값
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = night_withdtaw(balance, 500)
print("수수료는 {}원이며, 잔액은{}입니다.".format(commission, balance))

# 기본값
def profile(name, age, lang):
    print("name : {}, age : {}, lang :{}".format(name, age, lang))

profile("yoo" , 20 , "python")
profile("kim" , 25 , "java")

# 같은나이, 같은언어
def profile(name, age = 17, lang = "python"):
    print("name : {}, age : {}, lang :{}".format(name, age, lang))

profile("kim")
profile("yoo")

# 가변인자
def profile(name, age, *language):
    print("name:{} age:{}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")


profile("yoo", 20, "python", "java", "c++", "c#", "javascript")
print("kim", 25, "kotlin", "swift")

# 지역변수(함수가 끝나면 사라짐), 전역변수(모든공간에서 사용)
gun = 10

def checkpoint(soldiers):  # 총을 들고 경계근무나가는 군인
    global gun
    gun = gun - soldiers
    print("남은 총 :{}".format(gun))

print("전체 총:{}".format(gun))
checkpoint(2) # 2명이 경계근무
print("남은 총:{}".format(gun))

gun = 20
def checkpoint_return(gun, soldiers) :
    gun = gun - soldiers
    print("남은 총:{}".format(gun))
    return gun

gun = checkpoint_return(gun, 14)
print("남은 총:{}".format(gun))

# 표준체중 구하기
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21
# 조건 1) 함수명 : std_weight , 전달값 : 키, 성별

def std_wight(gender, height):
    if gender == "여자" :
        print("키{}cm {}의 표준체중은 {}입니다.".format(height, gender, round(height/100 * height/100 *21), 2))
    else:
        print("키{}cm {}의 표준체중은 {}입니다.".format(height, gender, height/100 * height/100 *22))

std_wight("여자", 155)













