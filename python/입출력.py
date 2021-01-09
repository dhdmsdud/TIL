# 표준입출력
print("python","java",sep=",",end="?")
print("무엇이 더 재밌을까요?")

import sys
print("python","java",file=sys.stdout) # 표준출력
print("python","java",file=sys.stderr) # 표준에러

# .ljust() : 왼쪽으로 () 만큼 정렬 / .rjust : 오른쪽으로 () 만큼 정렬
scores = {"math":0, "english":50, "cording":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# .zfill() : ()만큼 빈 곳을 0으로 채움
# 은행 대기순번표 (001,002,003...)
for num in range(1, 21):
    print("대기번호 : ",str(num).zfill(3))

# input형태로 출력할때는 타입이 항상 문자열
answer = input("아무 값이나 입력 : ")
print("입력하신 값은",answer,"입니다.")

# 빈 자리는 빈공간으로 두고 오른쪽 정렬, 총 10자리 확보, 양수와 음수를 구별하며 500 출력
print("{0: >+10}".format(500))
# 왼쪽정렬, 빈칸엔_
print("{0:_<}".format(500))
# 3자리마다 콤마찍고 양음수 구분
print("{0:+,}".format(10000000000))
# 소수점 둘째자리까지 출력
print("{0:.2f}".format(5/3))

# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") #쓰기 파일 생성
print("math : 100", file=score_file)
print("english : 100", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # 파일에 내용 추가
score_file.write("science : 98")
score_file.write("\ncording : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 파일내용을 한번에 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 파일내용을 한줄씩 읽기
print(score_file.readline())

score_file = open("score.txt", "r", encoding="utf8") # 파일내용이 몇줄인지 모를떄
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 파일을 리스트형태로 출력
lines = score_file.readlines()
for line in lines:
    print(line, type(line))
score_file.close()

# pickle : 프로그램상 데이터를 파일형태로 저장
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"name" : "ruby", "age" : "25", "hobby" : ["piano", "sports", "game"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I'am studying python very hard.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 1~50주차까지의 보고서 파일을 만드는 프로그램
# -()주차 주간보고-
# 부서 :
# 이름 :
# 업무요약 :

for i in range (1, 51):
    work_file = open("{}주차.txt".format(i), "w", encoding="utf8")
    print("-{}주차 요약보고-".format(i), file=work_file)
    print("부서 : ", file=work_file)
    print("이름 : ", file=work_file)
    print("업무요약 : ", file=work_file)
work_file.close()
