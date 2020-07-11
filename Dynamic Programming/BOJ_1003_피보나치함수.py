# 1003 피보나치 함수

T = int(input())

dp = [0 for i in range(41)]


def fibonacci(n):
    global dp

    if type(dp[n]) is list:
        return dp[n]

    if n == 0:
        return [0, 1, 0]
    elif n == 1:
        return [1, 0, 1]
    else:
        temp1 = fibonacci(n - 1)
        temp2 = fibonacci(n - 2)
        dp[n] = [temp1[0] + temp2[0], temp1[1] + temp2[1], temp1[2] + temp2[2]]

    return dp[n]


for i in range(T):
    N = int(input())

    rtn = fibonacci(N)
    print(rtn[1], rtn[2])

    dp = [0 for j in range(41)]