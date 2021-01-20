# python sequence type - tuple
# 순서, 중복가능 / 수정, 삭제 불가능
# 불변, 읽기전용
# ()

mytuple = ('반도', '강철비2', '아이언맨')
onetuple = (1,)

# 사용자의 편의를 위해 괄호없이 만들수 있음
mytuple = 1,2,3,4,5
multituple = (100, 1000, 'ace', 'base', 'captine')
print('tuple print -' , multituple)

# indexing
print(('index 1 - ' , multituple[1]))
print('slicing - ' , multituple[2:5] , type(multituple[2:]))

# casting
multilist = list(multituple[2:])
castingmultituple = tuple(multilist)

# python sequence type - range
# 1~99까지의 정수 중 짝수만 저장된 튜플
range01 = range(10)
print(range01)

range02 = range(1, 11, 2)
print(range02)

even = tuple(range(2, 100, 2))
print(even)
# even[0] = 1 ==> error

print(7 in range02)
print(range02.index((7)))
print(range02[2])
print(range02[2:])
print(range02[-1])










