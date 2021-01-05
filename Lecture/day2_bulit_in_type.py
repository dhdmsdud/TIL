# 변수정의 및 설정
# 블럭단위 런 : shift + alt + e
intvalue = 123
floatvalue = 3.14
boolvalue = True
strvalue = 'dmsdud'
print(type(intvalue), type(floatvalue), type(boolvalue), type(strvalue))

# type string
numStr = '720'
numNum = 100
print(int(numStr) + numNum) #문자를 숫자로
print(numStr + str(numNum)) #숫자를 문자로

year = '2021'
print(int(year) - 1)

# list[]
listAry = ['python' , 'anaconda']
print(type(listAry))

# dict{}
dictvalue = {
    "name" : "machine learning" ,
    "version" : 2.0
}
print(type(dictvalue))

# tuple()
tuplevalue = (3,)
print(type(tuplevalue))

# set{}
setvalue = {3,5,7}
print(type(setvalue))

# input()
inputNumber = int(input('숫자 : 100'))
sum = 100 + inputNumber
print(sum)

# str
str01 = 'i am python'
str02 = "python"
str03 = '''this is a
nultiline
sample test'''
str04 = """this is a 
multiline
sample test"""

seqtext = 'talk is chaep. show me the code'
print(seqtext)

# dir()
print(dir(seqtext))

# slicing
print(seqtext[3])
print(seqtext[-1])
print(seqtext[0:4])
print(seqtext[-6: ])
print(seqtext[: : -2]) # a이상 b미만 c만큼 건너뛰면서
print(seqtext[::2])

# 아래 문자열에서 '홀'만 출력 , 반대로 출력 , '짝'만 출력
string = '홀짝홀짝홀짝홀짝'
print(string[::2])
print(string[::-1])
print(string[1::2])

# 문자열 조작을 위한 많은 내장함수 제공
string = "python"
print("capitalize : " , string.capitalize())

str = 'dmsdud'
print('angel : ' , str.capitalize())

a = '녕'
print('princess : ' , a.capitalize())

# 문자치환 replace(oldchar, newchar)
phonenumber = '010-1234-5678'
replacephonenumber = phonenumber.replace('-' , '')
print(replacephonenumber)

string = 'abcdefg2a3c3v'
print( string.replace('a' , 'A'))

# 문자열을 쪼개는 함수 : split()
url = 'http://www.naver.com'
urlsplit = url.split('.')
print(urlsplit)
print(urlsplit , type(urlsplit))
print('domain : ' , urlsplit[-1])

num = '010-1234-5678'
numsplit = num.split('-')
print(numsplit)
print('middle:' , numsplit[1])

# 공백제거 함수 : strip(), rstrip(), lscrip()
# 대소문자 변환함수 : upper(), lower()
companyname = '    samsung    '
print(companyname.strip() , len(companyname.strip()))
print(companyname.rsplit() , len(companyname.rstrip()))
print(companyname.lstrip() , len(companyname.lstrip()))
print(companyname.upper())

# endwith()
filename = 'report.xls'
isexits = filename.endswith(('xls' , 'xlsx'))
print(isexits, type(isexits))

# in, not in : 해당 문자열에 있는지 없는지
mystr = 'this is a sample text'
print('sample' in mystr)

# 문자의 빈도 count(), 문자찾기 find(), 문자의 인덱스 index()
brandname = 'cocacola'
print(len(brandname) , brandname.count('c') , brandname.find('f') , brandname.index('a'))
