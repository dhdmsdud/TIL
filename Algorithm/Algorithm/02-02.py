### 클래스와 함수 선언
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


### 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["은영", "유로", "제니", "사나", "지효"]


### 메인 코드
# 첫 번째 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

# 두 번째 이후 노드
for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
