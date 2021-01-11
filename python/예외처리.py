# 예외처리
try:
    print("나누기 계산기")
    num1 = int(input("첫번째 숫자를 넣으세요. : "))
    num2 = int(input("두번째 숫자를 넣으세요. : "))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알수없는 에라기 발생했습니다")
    print(err)

# 에러 발생시키기
try:
    print("한자리 숫자 나누기 계산기")
    num1 = int(input("첫번째 숫자를 넣으세요. : "))
    num2 = int(input("두번째 숫자를 넣으세요. : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")

# 사용자정의 예외처리
class Bignumber_error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
try:
    print("한자리 숫자 나누기 계산기")
    num1 = int(input("첫번째 숫자를 넣으세요. : "))
    num2 = int(input("두번째 숫자를 넣으세요. : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError("입력값{}, {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except Bignumber_error as err:
    print("에러가 발생했습니다. 한자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") # finally: 예외처리중에서 정상이거나 오류거나 상관없이 무조건 실행

#####
class SoldoutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
     try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨을 몇마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {}] {} 마리 주문이 완료됐습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldoutError
     except ValueError:
         print("잘못된 값을 입력했습니다.")
     except SoldoutError:
         print("재고가 소진되어 더이상 주문을 받지 않습니다.")
         break
