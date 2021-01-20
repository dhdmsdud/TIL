# open(file = '파일경로/파일명', mode='r|w|a|wb')
# 텍스트파일 입출력

file = open("hello.txt", 'w')
file.write('hi, ruby')
file.close()
#
# file = open("hello.txt", "r")
# print(file.read())
# file.close()

# with open() as file : close를 하지 않아도 됨
# with open("hello.txt", "r") as file:
#         print(file.read())

# def file_stream(file_name, mode):
#     if mode == "w":
#         pass
#     elif mode == "r":
#         with open(file=file_name, mode=mode) as file :
#             line = file.read()
#             print(line)
#     elif mode == 'a' :
#         pass
#     else:
#         raise Exception("모드를 확인하세요")

#####
def file_stream(file_name, mode): # 예외가 있을때
    try:
        if mode == "w":
            file = open(file=file_name, mode=mode)
            file.write("happy")
        elif mode == "r":
            file = open(file=file_name, mode=mode)
            line = file.read()
            print(line)
        elif mode == "a":
            file = open(file=file_name, mode=mode)
            file.write('\nappend')
        else:
            raise Exception("모드를 확인하세요")
    except Exception as e :
        print(e)
    finally:
        if file != None:
            file.close()

#####
def withmultiwriter(file_name):
    with open(file_name, "w", encoding="utf8") as file :
        for  idx in range(3):
            print(idx)
            text = input("문자열 입력하세요")
            file.write('{} - {}\n'.format(idx, text))

#####
def with_list_file_writer(file_name, dataset):
    with open(file_name, "w", encoding="utf8") as file:
        for idx in range(len(dataset)):
            print(idx)
            file.write("{} - {}\n".format(idx, dataset[idx]))

#####
def with_list_file_read(file_name, mode): #방법1
    with open(file_name, mode, encoding="utf8") as file:
        line = None
        while line != "":
            line = file.readline()
            print(line.strip("\n"))

def with_list_file_read(file_name, mode): #방법2
    with open(file_name, mode, encoding="utf8") as file:
        for line in file.readlines():
            print(line.strip("\n"))

def with_list_file_read(file_name, mode): #방벙3
    with open(file_name, mode, encoding="utf8") as file:
        for line in file:
            print(line.strip("\n"))