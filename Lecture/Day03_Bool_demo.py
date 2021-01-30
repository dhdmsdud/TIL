# python bool type
# True(T) , False(F)
# not , and , or : 논리연산
# & , : , ~ : 비교연산
# False로 간주 : 비어있는 "" , [] , () , {} , 숫자(0을 제외한 숫자는 True) , None

xvalue = 5 # 0101
yvalue = 0 # 0000 = 0000 = 0
           # 0000 = 0101 = 5
print(xvalue & yvalue)
print(bool(xvalue & yvalue))
print(xvalue | yvalue)
print(bool(xvalue | yvalue))

truevalue = True
falsevalue = False
print(int(truevalue)) #1은 의미x
print(int(falsevalue))
print(truevalue & falsevalue)
print(truevalue | falsevalue)
print(truevalue and falsevalue)
print(truevalue or falsevalue)
print(not truevalue)







