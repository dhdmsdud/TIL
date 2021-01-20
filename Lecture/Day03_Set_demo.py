# python set type -set(집합)
# 순서,중복x
# set([]) , {}
temp = {'dmsdud' , 'student'}
print(temp , type(temp))

temp = set([1,2,3,4,5,5,5,5,5])  # set은 중복 허용x이므로 5가 한번출력
print(temp , type(temp))

temp = set([1,3.14,'pen',False])  # 순서x이므로 무작위로 출력
print(temp , type(temp))
casting = tuple(temp)
print(casting , casting[1:3] , type(casting))

# 교집합(intersection) : & / 합집합(union) | : / 차집합(difference) : -
# 객체(변수, 함수)
# 객체.변수 / 객체.함수()
set01 = set([1,2,3,4,5])
set02 = set([3,4,5,6,7])
print(set01&set02)  # 교집합==>{3,4,5}
print(set01.intersection(set02))
print(set01.union(set02)) # 합집합==>{1,2,3,4,5,6,7}
print(set01-set02)  # 차집합==>{1,2}
print(set01.difference(set02))

# 요소추가 : add / 요소삭제 : remove() , discard()
# 중복제거용으로도 사용가능
# set01.remove(9) ==> 없는요소에 대해 삭제하려고 할때 에러
# set.discard(9) ==> 에러x
set01.add(7)
print(set01)
set01.remove(4)
print(set01)
a = ['홀','짝','홀','짝','홀','짝','홀','짝']
seta = set(a)
print(seta , type(seta))
lista = list(seta)
print(lista , type(lista))
print(lista[0])
print(lista[1])