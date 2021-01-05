# python mapping type - dict
# dictionary는 key, value의 대응관계
# Hash or Associative Array와 유사한 구조
# {}
# 순서x, 키중복 허용x, 수정 및 삭제o

temp = {}
print(type(temp))

dict01 = {
    'name' : 'dmsdud',
    'age' : 25,
    'address' : 'anyang',
    'birth' : '970710'
    }
print('dict -' , type(dict01) , dict01)

# dict에 요소추가
dict01['gender'] = 'w'
dict01['marriage'] = False
print('dict -' , type(dict01) , dict01)

# 키 유무를 파악
print('marriage' in dict01)

# 데이터 확인
print('address - ' , dict01['address'])
print('address - ' , dict01.get('name'))
print('len - ' , len(dict01))

dict03 = dict(
    name='dmsdud',
    age=20,
    address='anyang',
    birth='970710',
)
# dict_keys, dict_values, dict_items
print('dict_keys - ' , dict03.keys() , type(dict03.keys()) , type(list(dict03.keys())))
print('dict_values - ' , dict03.values() , type(dict03.values()) , type(list(dict03.values())))
print('dict_items - ' , dict03.items() , type(dict03.items()) , type(list(dict03.items())))

# looping
'''
for (초기식; 조건식; 증감식; {
}
for item in collection :
    statement
'''
for key in dict03.keys() :
    print('key : {} , value : {}'.format(key, dict03.get(key)))

for value in dict03.values() :
    print('value : {}'.format(value))

for (key , value) in dict03.items() :
    print('key : {} , value : {}'.format(key, value))

# 삭제 pop(), del
print('dict03 - ' , type(dict03) , dict03)
del dict03['gender']
print('dict03 del -' , type(dict03) , dict03)
print('dict03 pop -' , dict03.pop('birth'))
print('dict03 del - ' , dict03)







