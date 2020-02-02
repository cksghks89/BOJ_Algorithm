#BOJ 2667 단지번호붙이기
import sys

N = int(sys.stdin.readline())
G = []

def bfs(g, start, visit):
    global N
    count = 0
    s = []
    s.append([start[0], start[1]])
    while len(s) != 0:
        now = s.pop(0)
        if visit[now[0]][now[1]] == 0:
            visit[now[0]][now[1]] = 1
            g[now[0]][now[1]] = 0
            count += 1
            if now[0] != 0 and g[now[0] - 1][now[1]] == 1:
                s.append([now[0] - 1, now[1]])
            if now[0] != N-1 and g[now[0] + 1][now[1]] == 1:
                s.append([now[0] + 1, now[1]])
            if now[1] != 0 and g[now[0]][now[1] - 1] == 1:
                s.append([now[0], now[1] - 1])
            if now[1] != N-1 and g[now[0]][now[1] + 1] == 1:
                s.append([now[0], now[1] + 1])
    return count

for i in range(N):
    l = list(map(int, list(sys.stdin.readline().rstrip())))
    G.append(l)
visit = [[0 for i in range(N)] for j in range(N)]

allCount = 0
homeList = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            homeList.append(bfs(G, [i, j], visit))
            allCount += 1

homeList.sort()
print(allCount)
for i in homeList:
    print(i)