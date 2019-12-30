#BOJ 1912 연속합

n = int(input())
A = list(map(int, input().split()))

dpList = [0 for i in range(0,n)]
maxList = [0 for i in range(0,n)]

if n == 1:
    print(A[0])
else:
    # dpList의 이전값은 그 값을 포함한 연속합의 최대값이라고 가정한다
    """
    그렇다면 현재의 dpList값은 이전값과 현재입력값을 더한것과 현재입력값을 비교하여
    더 큰 것이 현재dpList의 값이 된다.
    """
    dpList[0] = A[0]
    for i in range(1, n):
        dpList[i] = max(dpList[i-1] + A[i], A[i])

    maxs = -1000
    for i in range(0,n):
        if maxs < dpList[i]:
            maxs = dpList[i]
    print(maxs)
