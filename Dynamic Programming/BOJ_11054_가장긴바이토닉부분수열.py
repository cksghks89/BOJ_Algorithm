#BOJ 11054 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(0,N)]
dp[0] = 1

for i in range(1, N):
    temp = 0
    for j in range(0, i):
        if A[i] > A[j]:
            if temp < dp[j]:
                temp = dp[j]
    dp[i] = temp+1
A.reverse()
dp2 = [0 for i in range(0,N)]
dp2[0] = 1
for i in range(1, N):
    temp = 0
    for j in range(0, i):
        if A[i] > A[j]:
            if temp < dp2[j]:
                temp = dp2[j]
    dp2[i] = temp+1

max = 0
dp2.reverse()
for i in range(0, N):
    if max < dp[i]+dp2[i]:
        max = dp[i]+dp2[i]

print(max-1)