# 딕셔너리를 활용해 txt 파일 만들기
ruby = {"name" : "ruby", "age" : 25, "gender" : "w", "hobby" : "game"}
def ruby_write():
    with open(file="ruby_info.txt", mode="w" ,encoding="utf8") as file:
        for (key, value) in ruby.items():
            file.write("{} : {}\n".format(key, value))
            print("complete")

ruby_write()

# txt 파일을 피클로 만들기 --> import pickle 을 통해서 가져와야함!
# pickle 파일이므로 인코딩 utf8은 따로 해주지 않음, mode 는 "wb"
# dump : pickle로 변환하겠다는 의미
import pickle
def ruby_info_pickle():
    with open(file="ruby_info.txt", mode= "wb") as file:
        pickle.dump(ruby, file)
    print("피클을 이용한 파일저장 완료")

ruby_info_pickle()

# pickle 파일을 읽기, mode 는 "rb"
# load : pickle의 파일을 읽는다는 의미
import pickle
def ruby_info_pickle_reade():
    with open(file="ruby_info.txt", mode="rb") as file:
        ruby = pickle.load(file)
        print("file roading - ", ruby)
    print("피클을 이용한 파일읽기")

ruby_info_pickle_reade()

##### 응용 #####
# cnt 파일에서 10자 이하인 단어의 갯수를 카운트하는 함수
def word_function():
    word_list = []
    with open(file="./word/cnt_words.txt", mode="r", encoding="utf8") as file:
        for word in file.readlines():
            if len(word) <= 10:
                word_list.append(word)
    print("10자 이하의 단어 갯수는 {}개 입니다.".format(len(word_list)))
    print(word_list)

word_function()

# cnt 파일에서 15자 이하인 단어의 갯수를 카운트하는 함수
def word15_function():
    word_list15 = []
    with open(file="./word/cnt_words.txt", mode="r", encoding="utf8") as file:
        for word in file.readlines():
            if len(word) <= 15:
             word_list15.append(word)
        print("15자 이하의 단어 갯수는 {}개 입니다.".format(len(word_list15)))
        print(word_list15)

word15_function()

# cnt 파일에서 5자 이하인 단어들의 갯수를 카운트하는 함수
def word5_function():
    word_list = []
    with open(file="./word/cnt_words.txt", mode="r", encoding="utf8") as file:
        for word in file.readlines():
            if len(word) <= 5:
                word_list.append(word)
    print("5자 이하의 단어의 갯수는 {}개 입니다.".format(len(word_list)))
    print(word_list)

word5_function()

# cnt 파일에서 8자 이하인 단어들의 갯수를 카운트하는 함수
def word8_function():
    word_list = []
    with open(file="./word/cnt_words.txt", mode="r", encoding="utf8") as file:
        for word in file.readlines():
            if len(word) <= 8:
                word_list.append(word)
    print("8자 이하의 단어의 갯수는 {}입니다.".format(len(word_list)))
    print(word_list)

word8_function()

# special_words.txt 파일에서 문자가 'c'가 포함된 단어를 출력하는 함수를 만들어서 호출
# 주의) 단어를 출력할 때는 등장한 순서대로 출력하며, 쉼표나 마침표는 출력하지 않는다.
# split : 문자열을 나눔 , strip : 제거함
def include_c():
    with open(file="./word/special_words.txt", mode="r", encoding="utf8") as file:
        words = file.read().split()
        for word in words:
            if "c" in word:
                print(word.strip(',.'))

include_c()

# special_words.txt 파일에서 문자가 'a'가 포함된 단어를 출력하는 함수를 만들어서 호출
def include_a():
    with open(file="./word/special_words.txt", mode="r", encoding="utf8") as file:
        words = file.read().split()
        for word in words:
            if "a" in word:
                print(word.strip(',.'))

include_a()

# special_words.txt 파일에서 문자가 'z'가 포함된 단어를 출력하는 함수를 만들어서 호출
def includ_z():
    with open(file="./word/special_words.txt", mode="r", encoding="utf8") as file:
        words = file.read().split()
        for word in words:
            if "z" in word:
                print(word.strip(',.'))

includ_z()

# zipcode.txt
# input() 이용해서 동 이름을 입력 받아서 해당하는 동의 주소를 출력하는 함수를 정의하고 호출
# 예시 ) 개포 입력 --> 개포 1동 , 개포 2동 ..etc 출력.
# startswith() : ()로 시작하는 / endswith() : ()로 끝나는
def address_function():
    dong = input("찾는 동을 입력하세요 : ")
    with open(file="./word/zipcode.txt", mode="r", encoding="utf8") as file:
        line = file.readline()
        while line:
            address = line.split()
            if address[3].startswith(dong) and address[3].endswith("동"):
                print(address)
            line = file.readline()

address_function()

# csv, excel 파일을 읽기
# file= 을 쓰지않고 바로 파일위치 입력
import  pandas as pd # pandas 라이브러리를 사용해야함!

bmi_data = pd.read_csv("./word/service_bmi.csv", encoding="utf8")
print(bmi_data.info())
print(bmi_data.head()) # 최상위 5개의 데이터 정보만 보여짐
print(bmi_data.tail()) # 최하위 5개의 데어터 정보만 보여짐

# 속성에 대한 접근 : series ->list와 유사
print(bmi_data.height, type(bmi_data.height)) # 방법1)
print(bmi_data["height"]) # 방법2)

# 키, 몸무게 평균
print(sum(bmi_data.height)/len(bmi_data.height), sum(bmi_data.weight)/len(bmi_data.weight))
print(sum(bmi_data["height"])/len(bmi_data["height"]), sum(bmi_data["weight"])/len(bmi_data["weight"]))

# 키, 몸무게 최대 / 최소
# 표현식을 두개 써야함!, 하나만 쓰면 에러
print(max(bmi_data.height), max(bmi_data.weight))
print(min(bmi_data.height), min(bmi_data.weight))

# label 빈도수
label_count = {}
for label in bmi_data.label:
    label_count[label] = label_count.get(label, 0)+1
    print(label_count)

# spam_data.csv -> encoding='utf8'이 아닌 'ms949'를 출력
# pandas 에서는 head를 무조건 첫번째 줄로 인식하기 때문에 header="None"으로 잡아줌!
import pandas as pd
spam_data = pd.read_csv("./word/spam_data.csv", header=None, encoding="ms949")
print(spam_data)
print(spam_data.info())
print(spam_data.head())
print(spam_data.tail())

# spam_data 타겟과 텍스트
target = spam_data[0]
print(target, type(target))
text = spam_data[1]
print(text, type(text))

# spam = 1, ham = 0 새로운 타겟 만들기
# list comprehension 에서 else 까지 써야할 때는 if가 앞에 위치!
target = [1 if t == "spam" else 0 for t in target]
print(target)