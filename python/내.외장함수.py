# list of python builtins 내장함수 사이트
# 내장함수 : input --> 사용자 입력을 받는 함수
language = input("어떤 언어를 좋아하세요?")
print("{}은 좋은 언어입니다.")

# 내장함수 : dir --> 어떤 객체를 넘겼을때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시
list = [1,2,3]
print(dir(list))

name = "ruby"
print(dir(name))

# list of python modules 외장함수 사이트
# 외장함수 : glob --> 경로 내의폴더, 파일목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 .py인 모든 파일

# 외장함수 : os --> 운영체제에서 제공하는 기본기능
import os
print(os.getcwd())

folder = "sample"
if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder) # 폴더삭제
    print("폴더를 삭제했습니다.")
else:
    os.makedirs(folder) # 폴더생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())

# 외장함수 : time --> 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

# 외장함수 : timedelta --> 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days=100) # 오늘부터 100일 후
print("만난지 100일은", today + td)