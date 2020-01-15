#BOJ 2331 반복수열
import sys

A, P = map(int, sys.stdin.readline().split())

D = [A]
ans = 0
while True:
    sum = 0
    A = list(str(D[len(D)-1]))
    for i in range(0, len(A)):
        sum += int(A[i]) ** P

    if sum not in D:
        D.append(sum)
    else:
        ans = D.index(sum)
        break

print(ans)