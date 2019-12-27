T = int(input())
for i in range(0,T):
    N = int(input())
    dp = [[0, 0] for i in range(0, N + 1)]
    input1 = input()
    input2 = input()
    input1 = list(map(int, input1.split()))
    input2 = list(map(int, input2.split()))

    dp[1][0] = input1[0]
    dp[1][1] = input2[0]

    for j in range(2,N+1):
        sum1 = sum2 = sum3 = sum4 = 0
        sum1 = input1[j-1] + dp[j-1][1]
        sum2 = input1[j-1] + dp[j-2][1]
        dp[j][0] = sum1 if sum1 > sum2 else sum2
        sum3 = input2[j-1] + dp[j-1][0]
        sum4 = input2[j-1] + dp[j-2][0]
        dp[j][1] = sum3 if sum3 > sum4 else sum4
    print(dp[N][0] if dp[N][0] > dp[N][1] else dp[N][1])