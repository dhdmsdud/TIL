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

def insertNodes(findData, insertData) :
    global memory, head, current, pre

    # 첫 번째 노드 삽입
    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간에 노드 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 마지막에 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node


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

insertNodes("은영", "솔라")
printNodes(head)
insertNodes("제니", "화사")
printNodes(head)
insertNodes("바보", "문별")
printNodes(head)