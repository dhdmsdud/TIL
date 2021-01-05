# python sequence type - list
# 자료구조에서 중요
# 파이썬에서는 배열이 존재x
# 1차원의 자료구조
# 순서(index 부여 0~), 중복, 수정, 삭제 가능
# []이용해서 변수 선언

a = list()
a = []

a = [1,2,3]
print(a , type(a))
print(a[0])
a[0] = 5
print(a[0])

# 요소추가 : append(), insert()
a.append(4) # list뒤에 추가
print(a)
a.insert(0, 6) # 원하는 자리에 추가
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# pop() : 기존 리스트에서 요소를 가져오고 삭제함
print("a - pop() : " , a.pop())
print("a - pop() : " , a)

# extend() : 기존 리스트에 요소추가
ex = [4,3]
a.extend(ex)
print('a - extend : ' , a)

movierank = ['원더우먼','해리포터','겨울왕국2','가타카','반도']
# 해당 리스트에 배트맨 추가
movierank.append('베트맨')
print('append - 배트맨' , movierank)

# 원더우먼과 해리포터 사이에 '씽' 추가
movierank.insert(1, '씽')
print('insert - 씽' , movierank)

# 반도 삭제
movierank.remove('반도')
print('remove - 반도' , movierank)

# 최대값, 최소값, 총합, 평균
scoredate = [1,2,3,4,5,6,7]
print("max" , max(scoredate))
print("min" , min(scoredate))
print("sum" , sum(scoredate))
print("mean" , sum(scoredate) / len(scoredate))
