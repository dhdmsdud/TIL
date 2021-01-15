# binary(2진법) 형식의 입출력
# 객체직력화(Serializable) -> file에 저장
# pickle : 객체직렬화를 도와주는 모듈

scores = {"kor" : 100, "eng" : 100, "math" : 100, "science" : 100 }
print(type(scores))
def pickle_write(): # scores를 txt형식으로 저장
    with open(file="scores.txt", mode="w", encoding="utf8") as file:
        for (key, value) in scores.items():
            file.write("{} : {}\n".format(key, value))
            print("complete!")
pickle_write()

#####
import pickle
def pickle_writer(): # scores를 pickle로 저장
    with open(file="dict_scores.txt", mode="wb") as file:
        pickle.dump(scores, file)
    print(("객체직렬화를 통한 파일저장"))
pickle_writer()

def pickle_reader(): # pickle에 저장된 scores를 읽기
    with open(file="dict_scores.txt", mode="rb") as file:
        scores = pickle.load(file)
        print(scores)
    print(("객체직렬화를 통한 파일읽기"))
pickle_reader()

# 단어가 줄 단위로 저장된 cnt파일에서 10자 이하인 단어의 갯수를 카운트하는 함수 구현 및 호출
def cnt_reader():
    word_list = []
    with open(file="./word/cnt_words.txt", mode="r", encoding="utf8") as file:
        for word in file.readlines():
            word = word.strip("\n")
            if len(word) <= 10:
                word_list.append(word)
    print("{}개 입니다.".format(len(word_list)))

cnt_reader()


# special에서 c가 포함된 단어를 풀력하는 함수를 만들어서 호출
# 단어를 출력할때는 등장한 순서대로 출력하며 ,. 은 출력하지 않는다.
def special_reader():
    with open(file="./word/special_words.txt", mode="r", encoding="utf8") as file:
        words = file.read().split()
        for word in words:
            if "c" in word:
                print(word.strip(',' and '.'))

special_reader()

# zipcode.txt - input()을 이용해서 동 이름을 입력받아 ex)개포 해당하는 동의 주소를 출력하는 함수를 정의하고 호출
# startswith() : 문자열이 어떤것으로 시작하는지, endswith() : 문자열이 어떤것으로 끝나는지
def search_addr_function():
    dong = input("찾는 동을 입력하세요 : ")
    with open(file="./word/zipcode.txt", mode="r", encoding="utf8") as file:
        line = file.readline()
        while line:
            address = line.split()
            if address[3].startswith(dong) and address[3].endswith("동"):
                print(address)
            line = file.readline()

search_addr_function()

# csv, execel 파일은 pandas lib사용
import pandas as pd

bmi_data = pd.read_csv(file="./word/service_bmi.csv", encoding="utf8")
print(bmi_data.info())
print(bmi_data.head()) # 최상위 5개의 데이터 정보만 보여짐
print(bmi_data.tail()) # 최하위 5개의 데어터 정보만 보여짐

# 속성에 대한 접근 : series
print(bmi_data.height, type(bmi_data.height))
print(bmi_data["weight"])
print(bmi_data["label"])

# 키, 몸무게 평균
print("키 {}, 몸무게{}".format(sum(bmi_data.height) / len(bmi_data.height),
                           sum(bmi_data['weight']) / len(bmi_data["weight"])))

# 키 최대, 몸무게 최대
print("max height : ", max(bmi_data.height))
print("max weight : ", max(bmi_data.weight))

# label의 빈도수
label_count = {}
for label in bmi_data.label:
    label_count[label] = label_count.get(label, 0) + 1
print("label count : ", label_count)

# spam_data.csv
spam_data = pd.read_csv(file="./word/spam_data", header=None, encoding="ms949")
print(spam_data.info())
print(spam_data.head())
target = spam_data[0]
print(target)
text = spam_data[1]
print(text)

# spam=1, ham=0 새로운 타겟을 만들고 싶다면
target = [1 if t == "spam" else 0 for t in target]
print(target)

# code clean : 문자열에 대한 정규표현식을 이용하여 문자를 제거하는 작업
# 정규표현식 -> import re
# 메타문자 : .(무엇이든 한글자를 의미) ^(시작문자 지정) *(0 또는 more) +(1이상) ? {0이거나 1개만 있거나} [] \ | () $
# [abc] : a또는 b또는 c로 시작하는 문자와 매치
# [0-5] : 0이상 5이하 / [^0-5] : 0이상 5이하와 매칭되는 반대(not) / ^[0-5] : 0이상 5이하로 시작되는 문자와 매치
# 문자클래스 : \d(숫자의 자릿수) \D(문자매칭의 자릿수) \w(문자 + 숫자) \W(문자 + 숫자가 아닌 문자매치) \s(공백)
# sub()
# match()
# search()
# findall()
# finditer()
# 010-0000-0000 -> ^\d{3}-\d{4}-\d{4}
import re

p = re.compile('[a-z]+')
match = p.match('python') # 대소문자 구별
print(match)

# 텍스트 전처리 (특수문자, 숫자, 공백, 영문제거)->한글만 추출
text = spam_data[1]
print(text)

def clean_text(str):
    str = re.sub('[,.?!:;]', ' ', str)
    print(str)
    str = re.sub('[0-9a-zA-Z]', ' ', str)
    print(str)
    str = ' '.join(str.split())
    print(str)

clean_data = [clean_text(t) for t in text]
print(clean_data)

# 엑셀 파일 입출력
import pandas as pd
kospi_data = pd.ExcelFile("./word/sam_kospi.xlsx")
kospi = kospi_data.parse('sam_kospi')
print(kospi.info())

from statistics import *
print("high mean : ", mean(kospi.High))

# json 파일 입출력 : 네트워크상에서 표준으로 사용되는 파일형식
# 구성 : {key : value}
# encoding : python(dict, list) -> json 문자열(json file) / dumps()
# decoding : json 문자열(json file) -> python(dict, list) / loads()
# import json

# python -> json
import json
user = {"id" : 1234, "name" : "은영"}
print(type(user))

jsonstr = json.dumps(user) # encoding
print(jsonstr, type(jsonstr))

python_object = json.loads(jsonstr) # decoding
print(python_object, type(python_object))
print(python_object["name"])
print(python_object["id"])

# usagov_bitly.txt
with open(file= "./word/usagov_bitly.txt", mode="r", encoding="utf8") as file:
    lines = file.readlines()
    # print(type(lines), len(lines))
    # print(lines[:5])
    # lines[string]
    rows = [json.loads(line) for line in lines]
    # print(type(rows[0]))
    # print(type(rows))
    for row in rows :
        for key, value in row.items():
            print("key{}, value{}".format(key, value))

with open(file= "./word/usagov_bitly.txt", mode="r", encoding="utf8") as file:
    lines = file.readlines()
    rows = [json.loads(line) for line in lines] # rows -> pd.dataframe(행렬)
    rowsDF = pd.data_frame(rows)

print(rowsDF.head)