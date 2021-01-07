# python control statment forlooping
# for ~ in range()
# for ~ in list, dict
# for ~ in enumerate(list)

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

# 단어의 빈도수 구하기
# get() : 해당key의 vqlue 값을 가져옴
wordvec = ['love' , 'word' , 'cat' , 'love' , 'love']
print(len(wordvec))
wordcnt = {}
for word in wordvec :
    wordcnt[word] = wordcnt.get(word,0) + 1
    print(wordcnt)

wordcnt02 = {}
for word in wordvec :
    if word in wordcnt02 :
        wordcnt02[word] = 1
    else:
        wordcnt02[word] = 1

# [list] , (tuple) , {set} , dict{key : value}
# 1 ~ 1000 sum
rangesum = 0
for value in range(1, 1001) :
    rangesum += value
    print('1 ~ 1000의 합 {} 입니다.'.format(rangesum))

# 2000 ~ 2050 까지 올림픽 개최년도 출력
# 한줄에 5개의 년도출력 개행
cnt = 0
for year in range(2000, 2051, 4) :
    cnt += 1
    print(year , end='\t')
    if cnt %5 == 0 :
        print()

# 세글자 이상의 단어만 출력
wordlist = ['i','am','study','pythone','laguage','!']
for word in wordlist :
    if len(word) >= 3 :
        print(word)
wordlist = ['i','am','study','PYTHON','laguage','IF','FOR']
for word in wordlist :
    if word.isupper() :
        print(word)

wordlist = ['dog','cat','pig','carrot','horse','!']
for word in wordlist :
    print(word.capitalize())

# 파일 확장자를 제거하고 파일이름만 출력
filelist = ['greeting.py','bool.py','intro.hwp','bigdate.doc','ai.doc']
for file in filelist :
    print(file, file.split('.'), file.split('.')[0])

word = 'Handsom Boy'
for w in word :
    if w.isupper() :
        print(w, end='.')

# 모든 문자를 대문자로
dumy = ['alkjfhlauhfwljaflAUHDO']
for w in dumy :
    if w.isupper() :
        print(w, end='')
    else :
        print(w.upper(), end='')

# 거꾸로 출력
wordlist = ['가','나','다','라']
for word in wordlist[::-1] :
    print(word)

# break : 특정조건을 찾고 루프를 멈춤 , continue : 특정조건을 만족했을때 제외하고 계속 루핑
search = 17
numbers = [14,3,4,7,10,24,17,2,33,34,36,57]
for num in numbers :
    if num == search :
        print('found - ' , num)
        break
    else :
        print('not found - ' , num)

for i in range(1, 6) :
    for j in range(1,4) :
        print('i - {} , j - {}'.format(i,j))

# for ~ else
search = 5
numbers = [14,3,4,7,10,24,17,2,33,34,36,57]

for num in numbers :
    if num == search :
        print('found - ' , num)
        break
else :
    print('not found - ' , search)

# 구구단 만들기
for i in range(2, 10) :
    for j in range(1, 10) :
        print('{}*{}={}'.format(i, j, ((i*j)), end='\t'))
     print()
    if i == 5 :
        break

# append():마지막 인덱스에 추가, insert():특정인덱스에 추가, extend():리스트의 요소추가
string ='''저는 여러분들과 함게 파이썬 강의중인 녕입니다.
어려운 시기에 함께 되어서 반갑습니당!
얼른 오프라인으로 보고싶네용'''
sentences = []
words = []
for s in string.split('\n') :
    sentences.append(s)
    for w in s.split() :
        words.append(w)
print(sentences , len(sentences))
print(words , len(words))

# 분류정확도
answer = [1,0,2,1,0]
predict = [1,0,2,0,0]
acc = 0
for idx in range(len(answer)) :
    fit = answer[idx] == predict[idx]
    #print (int(fit , end='\t'))
    acc += int(fit) * 20
print(acc)

# enumerate : 반복문 사용시 몇번째 반복문인지 확인이 필요하다면 인덱스번호, 컬렉션요소 확인 가능
booklist = ['sql','r','textmining','python','django','nlp']
for idx , book in enumerate(booklist) :
    print('index={} , value={}'.format(idx, book))

# while <expression> : 증감식
cnt = 5
while cnt > 0 :
    print(cnt)
    cnt = cnt -1
    print(cnt)

# list - pop() : 마지막 인덱스부터 뺴면서 제거
whilelist = ['foo', 'bar', 'baz']
while whilelist :
    print(whilelist.pop())
print('while end')

# 난수를 발생시켜 횟수내에 맞추는 게임
import random
ran = random.random() # 0~1 사이의 난수를 발생시키는 실수형
print(ran)

ran = random.randint(0, 2) #정수형
print(ran)

#숫자범위 : 1-10 / 내가 입력한 숫자 > 난수 / 내가 입력한 숫자 < 난수
randnum = random.randint(1, 10)
while True :
    usernum = int(input("예상숫자 입력 : "))
    if randnum == usernum :
        print("success")
        break
    elif randnum > usernum :
        print("more")
    else :
        print("less")

# 1-100사이의 난수 , 도전횟수 20회 제한 , 출력결과:정답시도횟수,정답
randnum = random.randint(1, 100)
tries = 1
while tries <= 20 :
    usernum = int(input("숫자입력 : "))
    if randnum == usernum :
        print("정답")
        break
    elif randnum > usernum :
        print("more")
    else:
        print("less")
    tries += 1
if usernum == randnum :
    print("정답 시도횟수{}".format(tries))
    print("정답{}".format(randnum))
else :
    print("정답{}".format(randnum))

# random.choices()
# 모집단 dateset에서 k개의 데이터를 샘플링
dataset = list(range(1, 1001))
train = random.choices(dataset , k=10)
print(train)
