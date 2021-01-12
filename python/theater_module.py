# 모듈의 확장자 : .py
# 일반 영화가격
def price(people):
    print("{}명 가격은 {}원 입니다.".format(people, people * 10000))

# 조조영화
def price_morning(people):
    print("{}명 조조 할인 가격은 {}원 입니다.".format(people, people * 6000))

# 군인할인
def price_soldier(people):
    print("{}명 군인 할이 가격은 {}원 입니다.".format(people, people * 4000))

