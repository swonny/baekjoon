# class Node(object):
#     def __init__(self, data):
#         self.prev = None
#         self.data = data
#         self.next = None

# class DoublyLinked_list(object):
#     def __init__(self):
#         self.head = None
#     def append(self, node):
#         if self.head: # head 있으면
#             curn = self.head
#             while curn.next:
#                 curn = curn.next
#             curn.next = node
#             node.prev = curn
#         else:
#             self.head = node


class Graph(dict): # 그래프 정의
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
    def add_vertex(self,v):
        self[v] = {}
    def add_edge(self,e):
        v, w = e
        self[v][w] = e
        self[w][v] = e

class Vertex(object): #노드 정의
    def __init__(self, label=''):
        self.label = label
    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
    
    __str__ = __repr__

class Edge(tuple): #간선 정의
    def __new__(cls, e1, e2):
        return tuple.__new__(cls,(e1,e2))
    
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
    
    __str__ = __repr__

# v = Vertex('v')
# w = Vertex('w')
# e = Edge(v, w)
# print(e)

n,m,v = map(int, input().split())

for _ in range(m):
    v,w = input().split()
    e = Edge(v, w)

print(e)