from sys import stdin

node, edge = map(int, stdin.readline().split())

adj = [[0 for _ in range(node)] for _ in range(node)]

for _ in range(edge):
    src, dest = map(int, stdin.readline().split())
    adj[src][dest] = 1
    adj[dest][src] = 1