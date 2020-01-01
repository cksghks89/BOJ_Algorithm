#BOJ 9461 파도반 수열

T = int(input())

for i in range(0,T):
    N = int(input())
    dpList = [0 for j in range(0,N+1)]

    if 1 <= N <= 3:
        print(1)
    elif N == 4 or N == 5:
        print(2)
    elif N == 6:
        print(3)
    elif N == 7:
        print(4)
    elif N == 8:
        print(5)
    else:
        dpList[1] = dpList[2] = dpList[3] = 1
        dpList[4] = dpList[5] = 2
        dpList[6] = 3
        dpList[7] = 4
        dpList[8] = 5
        for j in range(9, N+1):
            dpList[j] = dpList[j-1] + dpList[j-5]
        print(dpList[N])