N = int(input())

dp = [[0,0,0,0,0,0,0,0,0,0]]*(N+1)
dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1):
    dp[i] = [0,0,0,0,0,0,0,0,0,0]
    for j in range(0,10):
        for k in range(0,j+1):
            dp[i][j] = dp[i][j] + dp[i-1][k]

sum = 0
for i in range(0,10):
    sum += dp[N][i]

print(sum%10007)