#BOJ 2225 합분해

N, K = map(int, input().split())

dpList = [[0 for i in range(0, N+1)] for j in range(0, K+1)]

for i in range(0, N+1):
    dpList[1][i] = 1

for i in range(1, K+1):
    for j in range(0, N+1):
        for k in range(0,j+1):
            dpList[i][j] += dpList[i-1][j-k]

print(dpList[K][N]%1000000000)