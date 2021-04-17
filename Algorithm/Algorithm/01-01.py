# 친구추가 함수의 완성
kakao = ['다현', '정연', '쯔위', '사나', '지효', '모모']

def insert_data(position, friend) :
    kakao.append(None)
    klen = len(kakao)

    for i in range(klen-1, position, -1) :
        kakao[i] = kakao[i-1]
        kakao[i-1] = None

    kakao[position] = friend

print(kakao)
insert_data(2, '솔라')
print(kakao)
insert_data(6, '문별')
print(kakao)


# 친구삭제 함수의 완성
def delete_data(position) :
    klen = len(kakao)
    kakao[position] = None

    for i in range(position+1, klen) :
        kakao[i-1] = kakao[i]
        kakao[i] = None

    del (kakao[klen-1])

print(kakao)
delete_data(1)
print(kakao)
delete_data(3)
print(kakao)