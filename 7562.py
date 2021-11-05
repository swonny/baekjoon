I = int(input())
root = list(map(int, input().split()))
find = list(map(int, input().split()))

class Node(object): # tree를 위한 노드
    def __init__(self, data = []):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

n = Node(root)

# def dfs(root, find = []):
    

# print(n.data) # root 행렬 출력
# for i in range(4): # 한 root당 8개의 자식이 있음
#     x = 1 if i < 2 else 2
#     for j in range(2):
#         if 
#         child = [n.data[0], n.data[1]+1] # n.data[0] 은 C[m][n]에서 m을 의미(행렬을 저장한거니까), n.data[1]은 n을 의미

# 일반화 필요
n.add_child([n.data[0]-2, n.data[1]-1])
n.add_child([n.data[0]-2, n.data[1]+1])
n.add_child([n.data[0]-1, n.data[1]-2])
n.add_child([n.data[0]-1, n.data[1]+2])

n.add_child([n.data[0]+1, n.data[1]-2])
n.add_child([n.data[0]+1, n.data[1]+2])
n.add_child([n.data[0]+2, n.data[1]-1])
n.add_child([n.data[0]+2, n.data[1]+1])


print(n.children)

# if find in n.children:
#     print(n.children)

if n.children.count(find): # children 찾기
    print(n.children.index(find))

