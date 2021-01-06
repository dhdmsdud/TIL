# python control statment forlooping
# for ~ in range()
# for ~ in list, dict

usersum = 0
for tmp in range(1, 11) :
    usersum += tmp
print('누적 값은 : {} 입니다.'.format(usersum))

userlist = [1,2,3,4,5]
for tmp in userlist :
    print(tmp , end='\t')
    usersum += tmp
print('누적 값은 : {} 입니다.'.format(usersum))

usedict = {'name' : 'dmsdud' , 'gender' : 'w'}
for (key, value) in usedict.items() :
    print("{} , {}".format(key,value))

scores = [100,50,80,90,70,60]
for scores in scores :
    print(scores,end='\t')

for idx in range(len(scores)) :
    usersum += scores[idx]
print('scores 합 %d'% usersum)

# list comprehension
# for , if 구문을 통한 반복적인 표현식 이용가능
userlist = [1,2,3,4,5,6,7,8,9]
userlist02 = [tmp ** 2 for tmp in userlist]
print(userlist02)
userlist03 = [tmp **2 for tmp in userlist if tmp%2 == 0]
print(userlist03)

# dict에서도 사용가능
userdict = {'test' + str(tmp) : tmp ** 2for tmp in range(1,10)}
print(userdict)
