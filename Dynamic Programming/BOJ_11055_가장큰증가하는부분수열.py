#BOJ 11055 가장 큰 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [[0,0] for i in range(0,N+1)]
dp[0] = [1, A[0]]

for i in range(1,N):
    min = 0
    sum = 0
    for j in range(0,i):
        if A[i] > A[j]:
            if min < dp[j][0] and sum < dp[j][1]:
                sum = dp[j][1]
                min = dp[j][0]
    dp[i] = [min+1, sum+A[i]]
max = 0
for i in range(0, N):
    if max < dp[i][1]:
        max = dp[i][1]

print(max)