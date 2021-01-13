from ai.file.file_proc import *

# try: # file_proc에서 예외처리를 하지않고 caller 에서 했을때
#     file_stream("hello.txt", "r")
# except Exception as e:
#     print(str(e))
# print('end')

# file_stream("hello.txt", "a") # file_proc 에서 예외처리를 했을때
# print('end')

# withmultiwriter('multiline.txt')
# print('end')

# lines = ['hi','are you sleepy?','eat chocolate!!']
# with_list_file_writer('listline.txt', lines)

with_list_file_read("listline.txt", "r")