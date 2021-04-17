class Node() :
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = '은영'

node2 = Node()
node2.data = '다현'
node1.link = node2

node3 = Node()
node3.data = '제니'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# 중간에 노드 삽입
newNode = Node()
newNode.data = '유로'
newNode.link = node2.link
node2.link = newNode

# 노드 삭제
newNode.link = node3.link
del(node3)

current = node1
print(current.data, end=' ')
while current.link != None :
    current = current.link
    print(current.data, end=' ')

