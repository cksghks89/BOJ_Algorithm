#BOJ 11052 카드 구매하기

N = int(input())
P = list(map(int, input().split()))

dpList = [0 for i in range(0, N+1)]
P.insert(0,0)
dpList[1] = P[1]

for i in range(2, N+1):
    max = P[i]

    for j in range(1, int(i/2) + 1):
        if max < dpList[j] + dpList[i-j]:
            max = dpList[j] + dpList[i-j]
    dpList[i] = max

print(dpList[N])