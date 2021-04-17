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

def deleteNode(deleteData) :
    global memory, head, current, pre

    # 첫 번째 노드 삭제
    if head.data ==deleteData :
        current = head
        head = head.link
        del(current)
        return

    # 중간 노드 삭제
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return


### 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["은영", "유로", "제니", "사나", "지효"]


### 메인 코드
# 첫 번째 노드
node = Node()
node.data = dataArray[0]
head = nodememory.append(node)

# 두 번째 이후 노드
for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
deleteNode("사나")
printNodes(head)
deleteNode("지효")
printNodes(head)