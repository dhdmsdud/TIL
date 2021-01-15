# palindrom(회문) : 단어를 거꾸로 읽어도 같은 단어 또는 문장
# 기준이 필요(중앙을 기준으로해서 첫 글자와 마지막 글자를 비교) --> 반복문 필요
# // : 나눈것의 몫
str = "ruby0710"
idx = len(str) //2
print(idx, str[idx])

# 회문방법 1.
def ispalindrom():
    is_flag = True
    word = input("회문검사를 위헌 단어를 압력하세요. : ")
    for idx in range (len(word//2)):
        if word[idx] != word[-1-idx]:
            is_flag = False
            break

    return  is_flag

# 회문방법 2.
def reverse_palindrom():
    word = input("회문검사를 위헌 단어를 압력하세요. : ")
    print(word == word[::-1])

def reverse_palindrom02():
    word = input("회문검사를 위헌 단어를 압력하세요. : ")
    print(type(reversed(word), reversed(word)))
    print(list(word), list(reversed(word)))
    print(list(word) == list(reversed(word)))

# palindrom_words.txt 파일을 읽어 회문인 단어만 출력
def palindrom_file():
    with open(file="./word/palindrome_words.txt", mode="r", encoding="utf8") as file:
        for line in file:
            line = line.strip("\n")
            if line == line[::-1]:
                print(line)

# 문자열에서 2-gram 개의 연속된 요소를 추출
# 자연어 처리에서 많이 사용
# hekko -->he/el/ll/lo

text = 'hello'
for idx in range(len(text) -1):
    print(text[idx], text[idx+1], sep="")

text = "this is python project"
textlist = text.split()
print(type(textlist), textlist)

for idx in range(len(textlist)-1):
    print(textlist[idx], textlist[idx+1])

# zip()
num = [1,2,3,4]
name = ["hong", "gil","dong", "guy"]

dict = {}
for key, value in zip (num, name):
    dict[key] = value
print(dict)

# input을 활용해서 문자열을 입력
# python is a programming language that lets you work quickly
# input을 활용해서 gram 할 숫자를 입력받고 입력된 숫자에 해당하는 단어를 튜플형식으로 출력
# 입력된 문자열의 단어갯수가 입력된 정수 미만이라면 예외를 발생
def zip_ngram():
    sentences = input("sentences : ")
    gram = int(input("gram : "))
    words = sentences.split()
    for idx in range(len(words)-gram+1):
        print(words[idx : idx+gram])

def zip_ngram02():
    sentences = input("sentences : ")
    gram = int(input("gram : "))
    words = sentences.split()
    ngram = zip(*[words[idx:] for idx in range(gram)]) # * : 그램에 맞춰 컴마를 찍음
    # print(list(ngram))
    for idx in ngram:
        print(idx)