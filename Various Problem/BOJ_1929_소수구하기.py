#BOJ 1929 소수 구하기
import sys, math

M, N = map(int, sys.stdin.readline().split())

li = []
for i in range(0, N+1):
    li.append(i)
li[0] = li[1] = 0
T = math.sqrt(N)

for i in range(2, N+1):
    if li[i] != 0:
        for j in range(2*i, N+1, i):
            li[j] = 0

for i in range(M, N+1):
    if(li[i] != 0):
        print(li[i])
