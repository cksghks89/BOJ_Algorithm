#BOJ 11722 가장 긴 감소하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(0,N)]
dp[0] = 1

for i in range(1, N):
    temp = 0

    for j in range(0, i):
        if A[i] < A[j]:
            if temp < dp[j]:
                temp = dp[j]
    dp[i] = temp+1

max = 0
for i in range(0,N):
    if max < dp[i]:
        max = dp[i]

print(max)