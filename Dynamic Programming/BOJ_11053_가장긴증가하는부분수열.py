#BOJ 11053 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(0,N+1)]
dp[0] = 1

for i in range(1,N):
    min = 0

    for j in range(0,i):
        if A[i] > A[j]:
            if min < dp[j]:
                min = dp[j]
    dp[i] = min+1
max = 0
for i in range(0, N):
    if max < dp[i]:
        max = dp[i]

print(max)