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


SIZE = 5
stack = ['choco', None, None, None, None]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
print(stack)
retData = pop()