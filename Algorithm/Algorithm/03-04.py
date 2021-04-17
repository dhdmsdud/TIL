# 스택 용량 확인 : 차있는지
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False


# 스택 용량 확인 : 비어있는지
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False


# 스택에 데이터 넣기
def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('full stack')
        return
    top += 1
    stack[top] = data


# 스택 추출
def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('empty stack')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('empty stack')
        return None
    return stack[top]


# 전역변수 선언
SIZE = int(input('스택 크기 입력'))
stack = [None for _ in range(SIZE)]
top = -1

# 메인코드
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
