#BOJ 10451 순열사이클
import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    P = list(map(int, sys.stdin.readline().split()))
    P.insert(0,0)

    G = [0 for i in range(0, N+1)]
    for j in range(1, N+1):
        G[j] = P[j]

    count = 0
    visit = []
    for j in range(1, N+1):
        if j not in visit:
            visit.append(j)
            now = j
            while True:
                now = G[now]
                if now in visit:
                    break
                else:
                    visit.append(now)
            count += 1

    print(count)