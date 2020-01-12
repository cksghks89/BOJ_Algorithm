#BOJ 1260 DFS와 BFS
import sys
import queue


def bfs(g, start):
    visit = []
    q = queue.Queue()
    q.put(start)

    while q.qsize():
        now = q.get()
        if now not in visit:
            visit.append(now)
            for i in g[now]:
                q.put(i)
    return visit


def dfs(g, start):
    visit = []
    stack = queue.LifoQueue()
    stack.put(start)
    while stack.qsize():
        now = stack.get()
        if now not in visit:
            visit.append(now)
            for i in g[now]:
                stack.put(i)
    return visit


N, M, V = map(int, sys.stdin.readline().split())

G = {}
for i in range(0,N):
    G[i+1] = []

for i in range(0, M):
    v1, v2 = map(int, sys.stdin.readline().split())
    G[v1].append(v2)
    G[v2].append(v1)

for i in range(0, N):
    G[i+1].sort()
ansBFS = bfs(G, V)

for i in range(0, N):
    G[i+1].reverse()
ansDFS = dfs(G,V)
print(" ".join(map(str, ansDFS)))
print(" ".join(map(str, ansBFS)))
