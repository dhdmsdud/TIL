# 스택 용량 확인
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else:
        return False

# 스택에 데이터 넣기
def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('full stack')
        return
    top += 1
    stack[top] = data


SIZE = 5
stack = ['choco', 'green tea', 'strawberry', 'coffee', None]
top = 3

print(stack)
push('honey')
print(stack)
push('mint')
print(stack)