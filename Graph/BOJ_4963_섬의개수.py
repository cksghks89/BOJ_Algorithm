# BOJ 4963 섬의 개수
import sys

def bfs(g, start, visit, n, m):
    queue = []
    queue.append([start[0], start[1]])
    while len(queue) != 0:
        now = queue.pop(0)
        g[now[0]][now[1]] = 0
        if visit[now[0]][now[1]] == 0:
            visit[now[0]][now[1]] = 1
            if now[0] != 0 and g[now[0]-1][now[1]] == 1:
                queue.append([now[0]-1, now[1]])
            if now[0] != 0 and now[1] != n-1 and g[now[0]-1][now[1]+1] == 1:
                queue.append([now[0]-1, now[1]+1])
            if now[0] != 0 and now[1] != 0 and g[now[0]-1][now[1]-1] == 1:
                queue.append([now[0]-1, now[1]-1])
            if now[1] != 0 and g[now[0]][now[1]-1] == 1:
                queue.append([now[0],now[1]-1])
            if now[1] != n-1 and g[now[0]][now[1]+1] == 1:
                queue.append([now[0],now[1]+1])
            if now[0] != m-1 and now[1] != 0 and g[now[0]+1][now[1]-1] == 1:
                queue.append([now[0]+1, now[1]-1])
            if now[0] != m-1 and g[now[0]+1][now[1]] == 1:
                queue.append([now[0]+1, now[1]])
            if now[0] != m-1 and now[1] != n-1 and g[now[0]+1][now[1]+1] == 1:
                queue.append([now[0]+1, now[1]+1])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    G = []
    for i in range(h):
        G.append(list(map(int, sys.stdin.readline().split())))

    count = 0
    visit = [[0 for i in range(w)] for j in range(h)]

    for i in range(h):
        for j in range(w):
            if G[i][j] == 1:
                bfs(G, [i,j], visit, w, h)
                count += 1

    print(count)