#BOJ 9466 텀 프로젝트
import sys
sys.setrecursionlimit(10**6)
# -1 : 사이클,  nodeNumber : 방문,  0 : 방문 안함
T = int(sys.stdin.readline())


def dfs(g, start, v, temp):
    now = g[start]
    if v[start] == 0:
        v[start] = temp
        dfs(g, now, v, temp)
    elif v[start] == temp:
        v[start] = -1
        dfs(g,now,v,temp)
    else:
        return


for t in range(0, T):
    n = int(sys.stdin.readline())
    G = list(map(int, sys.stdin.readline().split()))
    G.insert(0,0)
    visit = [0 for i in range(0, n+1)]

    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(G, i, visit, i)
    count = 0
    for i in range(1, n+1):
        if visit[i] == -1:
            count += 1
    print(n-count)