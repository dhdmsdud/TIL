### 선형 리스트 구현
# 배열에 친구 추가
kakao = []
def add_data(friend) :
    kakao.append(None)
    klen = len(kakao)
    kakao[klen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(kakao)


