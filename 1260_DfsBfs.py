from collections import deque

deque1 = deque()

n, m, root = map(int, input().split())
graph = {}

for i in range(m): # 그래프 양방향 연결
    v1, v2 = map(int, input().split())
    if v1 not in graph:
        graph[v1] = list()
    if v2 not in graph:
        graph[v2] = list()
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = {} # visited 만들기
for i in list(graph.keys()):
    visited[i] = False

# print(visited)

# print(graph)

def bfs(v):
    visited[v] = True
    print(v,end=' ')
    # print(visited[v])
    temp = graph[v]
    for i in temp: # 인접 정점 큐에 삽입
        # print(i)
        if visited[i] == False: 
            # print(visited[i])
            deque1.append(i)
        # print(deque1)
    while deque1:
        # bfs(deque1.popleft())
        t =  deque1.popleft()
        # bfs(t if visited[t] == False else)
        if visited[t] == False:
            bfs(t)
        else:
            break

bfs(root)


# print(visited)

# key = 1

# print(graph[key])