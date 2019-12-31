#BOJ 1699 제곱수의 합

import math

N = int(input())

dpList = [0 for i in range(0,N+1)]
dpList[1] = 1

for i in range(2, N+1):
    integer = int(math.sqrt(i))
    min = 100000
    for j in range(1, integer+1):
        if min > dpList[i - j*j]:
            min = dpList[i - j*j]
    dpList[i] = min+1

print(dpList[N])