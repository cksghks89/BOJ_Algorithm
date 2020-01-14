#BOJ 1707 이분 그래프
import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())
count = 0
rtn = True
def dfs(g, start, color, visit):
    global count
    global rtn
    visit[start] = color
    count += 1
    if count == len(visit)-1:
        return

    for i in g[start]:
        if visit[i] == 0:
            dfs(g, i, color % 2 + 1, visit)
        if visit[i] == color:
            rtn = False
            return
    return


for t in range(0, T):
    V, E = map(int, sys.stdin.readline().split())
    G = {}
    count = 0
    rtn = True
    for i in range(0, V):
        G[i] = []
    for i in range(0, E):
        u, v = map(int, sys.stdin.readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    visit = [0 for i in range(0, V+1)]

    for i in range(0, V):
        if visit[i] == 0:
            dfs(G, i, 1, visit)

    if rtn:
        print("YES")
    else:
        print("NO")
