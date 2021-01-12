# "사회적 거리두기"에 따른 영화관 좌석예매 시스템을 만드시오.
# 각 열은 1 ~ 20 번까지 총 20개의 좌석으로 구성(a1,a2,a3...a20)
# 이 떄 a열에 대해 홀수로 끝나는 좌석에 대해서만 출력
for i in range(1, 21):
    if i % 2 == 1:
        print("A"+str(i), end=" ")

for i in range(1, 21)[::2]:
    print("A"+str(i), end=" ")

# 사람에 따라 메일 본문을 자동으로 써주는 프로그램을 만드시오.
names = ["you", "tu", "ber"]
for name in names:
    with open("{}.txt".format(name), "w", encoding="utf8") as email_file:
        email_file.write(f"""
안녕하세요? {name}님.

(주)은영출판 편집자 은영입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.
- 은영 드림.
        """)

# 신조어 퀴즈
class Word:
    def __init__(self, new_word, ex1, ex2, correct):
        self.new_word = new_word
        self.ex1 = ex1
        self.ex2 = ex2
        self.correct = correct

    def show_question(self):
        print("{}의 뜻은 무엇일까요?")
        print("1." + self.ex1)
        print("2." + self.ex2)
    def check_answer(self, user_input):
        if user_input != self.correct:
            print("틀렸습니다.")
        else:
            print("정답입니다.")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("==> ")))

# 행맨퀴즈
from random import *
words = ["cherry", "mango", "pineapple", "strawberry", "melon"]
word = choice(words)
print("answer : " + word)
letters = ""

while True:
    succeed = True
    print()
    for w in word :
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("success")
        break
    letter = input("input letter > ")
    if letter not in letters:
        letters += letter
    if letter in word:
        print("correct")
    else:
        print("wrong")