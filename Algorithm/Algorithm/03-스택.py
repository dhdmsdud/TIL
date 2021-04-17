# 스택 쌓기
stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = 'choco'
top += 1
stack[top] = 'green tea'
top += 1
stack[top] = 'strawberry'

print('스택')
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])