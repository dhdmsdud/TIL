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
