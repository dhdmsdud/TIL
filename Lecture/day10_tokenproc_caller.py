from ai.file.day10_tokenproc import *

# 회문방법 1.
palindrom_flag = ispalindrom()
if palindrom_flag :
    print("회문")
else:
    print("회문아님")

# 회문방법 2.
reverse_palindrom()

# 회문방법 3.
reverse_palindrom02()

# palindrom_words.txt 파일을 읽어 회문인 단어만 출력
palindrom_file()

zip_ngram()